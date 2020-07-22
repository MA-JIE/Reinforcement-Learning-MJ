# DQN
pytorch官网有QON算法详解以及代码实现: <br>
https://pytorch.org/tutorials/intermediate/reinforcement_q_learning.html <br>
中文文档: <br>
https://pytorch.apachecn.org/docs/1.0/reinforcement_q_learning.html <br>
相关博客: <br>
https://zhuanlan.zhihu.com/p/21421729 <br>
这篇应该是我看过这么多文章以来讲解的最为清晰的一篇了. <br>
# 算法框架图
![DQN](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E6%B7%B1%E5%BA%A6%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/DQN/img/DQN.jpg) <br>
Actions are chosen either randomly or based on a policy, getting the next step sample from the gym environment. We record the results in the replay memory and also run optimization step on every iteration. Optimization picks a random batch from the replay memory to do training of the new policy. “Older” target_net is also used in optimization to compute the expected Q values; it is updated occasionally to keep it current. <br>
# 算法详解
* 输入输出 <br>
它的输入是状态,输出是该状态下每个动作的Q值.<br>
* 经验回放 <br>
 经验回放就是把每一个时间步t的状态s_t，执行的动作a_t，获得的奖励r_t，以及s_t执行a_t到达的下一时间步的s_{t+1}组成四元组(s_t,a_t,r_t,s_{t+1})，放到一个回放池中，训练时，神经网络会从池中随机选出四元组作为训练数据，通过小批量梯度下降更新权重参数。这么做，而不是直接使用游戏过程中实时遇到的数据的好处主要有：<br>
(1) 打破了数据之间的相关性，也减少了随时间推移不同批次的训练数据差距过大的问题 <br>
(2) 数据利用率高，一条数据可以被多次利用 <br>
(3) 能够使神经网络利用很久以前的数据进行训练，克服了神经网络“健忘”的问题 <br>
* 固定目标网络 <br>
训练DQN的目的是使其能根据输入的state产生不同action的准确Q值。对于“准确Q值”的要求是，所有的Q值都必须满足贝尔曼方程。在DQN中，所有的Q值都是由同一个网络产生的，也就是说，DQN中的神经网络其实是做了两件事：产生预测值，产生标签。然而这就产生了一个问题，如果预测值和标签都是由一个网络产生的，那么当根据预测值和标签之间的loss更新网络权重时，标签也会会发生变化。如果预测值和标签同时变化，网络就不容易收敛。毕竟如果运动员和裁判是一个人，就没必要努力了是吧。因此，DQN用了两个网络，分别产生预测值和标签。论文中把产生预测值的网络叫做动作-值网络，把产生标签的网络叫做目标动作-值网络。这两个网络的结构是一样的，参数大部分时间是不一样的。我们训练的主要是动作-值网络，但是每隔一定的时间步就会把动作-值网络的参数赋值给目标动作-值网络。这样，目标动作-值网络的变化就不会很剧烈，促进了网络的收敛。事实上，GAN中也有同样的技巧。在GAN要训练生成器和判别器两个网络，我们选择每更新若干次判别器再更新一次生成器，这样也是为了使网络参数收敛. <br>
* 伪代码
![DQN](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E6%B7%B1%E5%BA%A6%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/DQN/img/DQN1.png) <br>
# pytorch代码解读
https://www.jianshu.com/p/a82a8b8ff78d <br>
