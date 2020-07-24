import gym
import math
import random
import matplotlib
import matplotlib.pyplot as plt
from collections import namedtuple
from itertools import count
from PIL import Image

import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torchvision.transforms as T

#不做unwrapped会有很多限制,unwrapped让开发人员能调整模型的底层数据，
# 例如解开reward的最大限制等。在这里加入或删除unwrapped无影响
env = gym.make('CartPole-v0').unwrapped
# print(env.action_space)  # Discrete(2)
# print(env.observation_space)  # Box(4,)
# print(env.observation_space.high
#       )  # [4.8000002e+00 3.4028235e+38 4.1887903e-01 3.4028235e+38]
# print(env.observation_space.low
#       )  # [-4.8000002e+00 -3.4028235e+38 -4.1887903e-01 -3.4028235e+38]

#set up matplotlib
is_ipython = 'inline' in matplotlib.get_backend()
if is_ipython:
    from IPython import display

plt.ion()

#if gpu is to be used
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

#类似c中的struct, Transitoin可以理解为一个类名
Transition = namedtuple('Transition',
                        ('state', 'action', 'next_state', 'next_action'))


# 经验回放池。把每条Transition（包括state，action，next_state，reward）放入池中，从中随机抽样来训练网络
# 使用经验回放目的是打破每一条数据之间的相关性。神经网络应该只关心在一条训练数据中，输入state与action所得到的reward，借此来调整神经网络的参数
# 例如在一个游戏中相邻两帧之间的数据就是有“有相关性的”数据。经验回放就是从一场游戏中抽取若干不相邻的帧
class ReplayMemory(object):
    def __init__(self, capacity):
        #经验回放池的最大容量
        self.capacity = capacity
        self.memory = []
        #列表下标
        self.position = 0
#若池中尚有空间，直接追加新数据，若无空间，则覆盖旧数据

    def push(self, **args):
        """save a transition"""
        if len(self.memory) < self.capacity:
            self.memory.append(None)
        self.memory[self.position] = Transition(*args)
        #覆盖旧数据
        self.position = (self.position + 1) % self.capacity


#随机抽样一个batch_size大小的数据集

    def sample(self, batch_size):
        return random.sample(self.memory, batch_size)

    def __len__(self):
        return len(self.memory)


class DQN(nn.Module):
    def __init__(self, h, w, outputs):
        super(DQN, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, kernel_size=5, stride=2)
        self.bn1 = nn.BatchNorm2d(16)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=5, stride=2)
        self.bn2 = nn.BatchNorm2d(32)
        self.conv3 = nn.Conv2d(32, 32, kernel_size=5, stride=2)
        self.bn3 = nn.BatchNorm2d(32)

        #线性输入连接的数量取决于conv2d层的输出，因此需要计算输入图像的大小,分别计算长宽的size

        def conv2d_size_out(size, kernel_size=5, stride=2):
            return (size - (kernel_size - 1) - 1) // stride + 1

        convw = conv2d_size_out(conv2d_size_out(conv2d_size_out(w)))
        convh = conv2d_size_out(conv2d_size_out(conv2d_size_out(h)))
        linear_input_size = convw * convh * 32
        self.head = nn.Linear(linear_input_size, outputs)

    def forward(self, x):
        x = F.relu(self.bn1(self.conv1(x)))
        x = F.relu(self.bn2(self.conv2(x)))
        x = F.relu(self.bn3(self.conv3(x)))
        return self.head(x.view(x.size(0), -1))


# 定义了一个流水线函数，把以下三个步骤整合到一起：1. 把tensor转为图像；
# 2.调整图像大小，把较短一条边的长度设为40；3.将图像转为tensor
resize = T.Compose(
    [T.ToPILImage(),
     T.Resize(40, interpolation=Image.CUBIC),
     T.ToTensor()])


#获取小车的中心位置，用于裁剪图像
def get_cart_location(screen_width):
    #小车左右横跳的宽度是4.8
    world_width = env.x_threshold * 2
    scale = screen_width / world_width
    #返回车子的中心
    return int(env.state[0] * scale + screen_width / 2.0)


# 获取环境的图像，可以不关注细节
def get_screen():
    # Returned screen requested by gym is 400x600x3, but is sometimes larger
    # such as 800x1200x3. Transpose it into torch order (CHW).
    screen = env.render(mode='rgb_array').transpose((2, 0, 1))
    # Cart is in the lower half, so strip off the top and bottom of the screen
    _, screen_height, screen_width = screen.shape
    screen = screen[:, int(screen_height * 0.4):int(screen_height * 0.8)]
    view_width = int(screen_width * 0.6)
    cart_location = get_cart_location(screen_width)
    if cart_location < view_width // 2:
        slice_range = slice(view_width)
    elif cart_location > (screen_width - view_width // 2):
        slice_range = slice(-view_width, None)
    else:
        slice_range = slice(cart_location - view_width // 2,
                            cart_location + view_width // 2)
    # Strip off the edges, so that we have a square image centered on a cart
    screen = screen[:, :, slice_range]
    # Convert to float, rescale, convert to torch tensor
    # (this doesn't require a copy)
    screen = np.ascontiguousarray(screen, dtype=np.float32) / 255
    screen = torch.from_numpy(screen)
    # Resize, and add a batch dimension (BCHW)
    return resize(screen).unsqueeze(0).to(device)


env.reset()
plt.figure()
# gpu中的tensor转成numpy数组必须移入cpu
plt.imshow(get_screen().cpu().squeeze(0).permute(1, 2, 0).numpy(),
           interpolation='none')
plt.title('Example extracted screen')
plt.show()
