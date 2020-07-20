import torch
import torch.nn as nn
from torch.distributions.categorical import Categorical
from torch.optim import Adam
import numpy as np
import gym
from gym.spaces import Discrete, Box


def mlp(sizes, activation=nn.Tanh, output_activation=nn.Identity):
    # Build a feedforward neural network.
    layers = []
    for j in range(len(sizes) - 1):
        act = activation if j < len(sizes) - 2 else output_activation
        layers += [nn.Linear(sizes[j], sizes[j + 1]), act()]
    return nn.Sequential(*layers)


def train(env_name="CartPole-v0",
          hidden_sizes=[32],
          lr=1e-2,
          epochs=50,
          batch_size=5000,
          render=False):
    # make environment, check spaces, get obs / act dims
    env = gym.make(env_name)
    # isinstance() 判断一个对象是否是一个已知的类型, assert false, "error"
    assert isinstance(env.observation_space, Box), \
        "This example only workd for env with continuous state space."
    assert isinstance(env.action_space, Discrete), \
        "This example only works for envs with discrete action space."
    obs_dim = env.observation_space.shape[0]
    n_acts = env.action_space.n
    # make core of policy network
    logits_net = mlp(sizes=[obs_dim] + hidden_sizes + [n_acts])

    # make function to compute action distribution
    def get_policy(obs):
        logits = logits_net(obs)
        return Categorical(logits=logits)

    # make action selection function(outputs int actions, sampled from policy)
    def get_action(obs):
        return get_policy(obs).sample().item()

    # make loss function whose gradient, for the right data, is policy gradient
    def compute_loss(obs, act, weights):
        #对应状态下采取动作act的概率
        logp = get_policy(obs).log_prob(act)
        return -(logp * weights).mean()

    # make optimizer
    optimizer = Adam(logits_net.parameters(), lr=lr)

    # for training policy
    def train_one_epoch():
        # make some empty lists for logging
        batch_obs = []  # for obsevation
        batch_acts = []  # for actions
        batch_weights = []  # for R(tau) weighting in policy gradient
        batch_rets = []  # for measuring episode returns
        batch_lens = []  # for measuring episode lenghts

        # reset episode-specific variables
        obs = env.reset()  # first obs comes from starting with current policy
        done = False  # signal from environment that episode is over
        ep_rews = []  # list for reward accrued throughout ep

        # render first episode of each epoch
        finished_rendering_this_epoch = False

        # collect experience by acting in the environment with current policy
        while True:
            # rendering
            if (not finished_rendering_this_epoch) and render:
                env.render()  # 图像引擎

            # save obs,状态集
            batch_obs.append(obs.copy())

            # act in the environment,当前状态通过神经网络后随机采样一个动作,这里act为对应索引
            act = get_action(torch.as_tensor(obs, dtype=torch.float32))
            #step(): 物理引擎, 输入: 动作a, 输出: 下一步状态，立即回报，是否终止，调试项
            obs, rew, done, _ = env.step(act)

            # save action,动作集 reward 回报集
            batch_acts.append(act)
            ep_rews.append(rew)

            #当每一幕终止时,我们有:
            if done:
                # if episode is over, record info about episode
                #求出一幕的回报和以及长度
                ep_ret, ep_len = sum(ep_rews), len(ep_rews)
                batch_rets.append(ep_ret)
                batch_lens.append(ep_len)

                # the weight for each logprob(a|s) is R(tau)
                batch_weights += [ep_ret] * ep_len

                # reset episode-specific variables
                #统计完一幕的数据后，重新设置
                obs, done, ep_rews = env.reset(), False, []

                # won't render again this epoch
                finished_rendering_this_epoch = True

                # end experience loop if we have enough of it
                # 当所有幕的状态总数大于batch_size时，终止
                if len(batch_obs) > batch_size:
                    break
            # take a single policy gradient update step
        optimizer.zero_grad()
        #每幕逐步执行，终止时计算整体的loss,
        batch_loss = compute_loss(obs=torch.as_tensor(batch_obs,
                                                      dtype=torch.float32),
                                  act=torch.as_tensor(batch_acts,
                                                      dtype=torch.int32),
                                  weights=torch.as_tensor(batch_weights,
                                                          dtype=torch.float32))
        batch_loss.backward()
        optimizer.step()
        print("batch_ocb's shape is: {}".format(batch_obs[0]))
        return batch_loss, batch_rets, batch_lens

    for i in range(epochs):
        batch_loss, batch_rets, batch_lens = train_one_epoch()
        print('epoch: %3d \t loss: %.3f \t return: %.3f \t ep_len: %.3f' %
              (i, batch_loss, np.mean(batch_rets), np.mean(batch_lens)))


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--env_name', '--env', type=str, default='CartPole-v0')
    parser.add_argument('--render', action='store_true')
    parser.add_argument('--lr', type=float, default=1e-2)
    args = parser.parse_args()
    print('\nUsing simplest formulation of policy gradient.\n')
    train(env_name=args.env_name, render=args.render, lr=args.lr)
