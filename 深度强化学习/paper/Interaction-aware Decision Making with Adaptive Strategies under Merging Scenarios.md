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
![decentralized critic]() <br>
* 在维持一个比较好的交通流的前提下，并道时与其他智能体更好地进行交互 <br>

(2)将两种目标函数整合 <br>
