# 深度强化学习
深度强化学习是深度学习与强化学习相结合的产物,它集成了深度学习在视觉等感知问题上强大的理解能力,以及强化学习的决策能力,实现了端到端学习.<br>
* 基于Q学习 <br>
* 基于策略梯度 <br>
* 基于探索与监督 <br>

# the on-policy algorithms
* VPG <br>
* TRPO  <br>
* PPO  <br>
A key feature of this line of work is that all of these algorithms are on-policy: that is, they don’t use old data, which makes them weaker on sample efficiency. But this is for a good reason: these algorithms directly optimize the objective you care about—policy performance—and it works out mathematically that you need on-policy data to calculate the updates. So, this family of algorithms trades off sample efficiency in favor of stability—but you can see the progression of techniques (from VPG to TRPO to PPO) working to make up the deficit on sample efficiency. <br>

# the off-policy algorithms
* DDPG  <br>
* TD3 <br>
* SAC <br>
Algorithms like DDPG and Q-Learning are off-policy, so they are able to reuse old data very efficiently. They gain this benefit by exploiting Bellman’s equations for optimality, which a Q-function can be trained to satisfy using any environment interaction data (as long as there’s enough experience from the high-reward areas in the environment). <br>
