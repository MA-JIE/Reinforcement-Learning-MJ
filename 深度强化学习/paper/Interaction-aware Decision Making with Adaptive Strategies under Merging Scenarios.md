# Interaction-aware Decision Making with Adaptive Strategies under Merging Scenarios
核心方法: <br>
an interaction-aware decision making with adaptive strategies (IDAS) approach
# 本文的贡献
(1)使用多智能体机制解决其他智能体driver model缺乏的问题 <br>
(2)引入驾驶风格(driver style)的概念去解决其他司机驾驶随机性的问题 <br>
(3)学习单一策略以获得一个可推广的决策机制，该决策机制可以在各种并道情况下应用自适应策略 <br>
(4)结合微观和宏观的视角，鼓励交互与合作 <br>
(5)利用curriculum learning(课程式学习)和掩码机制，提高学习效率 <br>
# Concept Clarification
作为输入: <br>
(1)Road priority <br>
(2)Driver type <br>
# Actor-Critic
引入actor-critic思想 <br>
参考知乎: https://zhuanlan.zhihu.com/p/36494307 <br>
actor: The actor is a parameterized policy that defines how actions are selected.<br>
critic: the critic is an estimated state-value function that criticizes the actions made by the actor.<br>
actor中的参数根据critic的评估来进行更新. <br>
# approach
#### Interaction-aware Decision Making(交互意识决策)
(1)定义了两种目标函数,类型如下: <br>
* 在并道场景中严格遵循交通规则 <br>
decentralized critic: The decentralized critic aimed to provide a policy gradient for agent to learn how to drive under merging scenarios by strictly following the rules while having different behaviors. <br>
智能体只专注与自身, 不与其他智能体进行交互,策略梯度公式如下: <br>
![decentralized critic](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E6%B7%B1%E5%BA%A6%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/paper/img/drl1.png) <br>
* 在维持一个比较好的交通流的前提下，并道时与其他智能体更好地进行交互 <br>
centralized critic: The centralized critic encourages each agent to interact with each other in order to have a joint success and maintain a smooth traffic. <br>
如果我们从宏观角度，比如交通流量上考虑，我们需要考虑与其他智能体交互的场景: <br>
![centralized critic](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E6%B7%B1%E5%BA%A6%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/paper/img/drl2.png) <br>
(2)将两种目标函数整合 <br>
整体策略梯度如下: <br>
![object function](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E6%B7%B1%E5%BA%A6%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/paper/img/drl3.png) <br>
#### Different Driving Behaviors
亮点:回报函数的定义方式，除了状态-动作对参数外，还包含了路权优先级b_prio以及驾驶风格b_type. <br>
每个智能体的回报函数由两个与驾驶行为相关的子回报函数组成：r_finish以及r_collide. <br>
#### Curriculum Learning
文中提到:尤其在多智能体场景下，让智能体同时去学习自适应性和交互性的驾驶行为的方式是困难和低效的,因此，基于课程式学习的策略，文中引入了双阶段的训练过程. <br>
![curriculum](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E6%B7%B1%E5%BA%A6%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/paper/img/drl4.png) <br>
#### Masking Mechanism
文中提到: 我们希望我们的策略能够直接学习如何在战术层面上做出决策，而不是去探索那些肯定会导致事故或打破规则的动作. <br>
三种掩码将会被考虑: 车辆动力学(保证无人车的加速度以及抖动在合理范围内)，交通规则(防止智能体超速)，安全因素(使智能体与前车保持安全距离) <br>
这样做的直接效果是，在选择最佳动作之前，我们应用掩码机制为了只选择可行动作的子集. <br>
最终的掩码为三个掩码的并集. <br>
