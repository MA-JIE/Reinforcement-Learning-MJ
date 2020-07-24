# Human-Like Decision Making for Autonomous Driving: A Noncooperative Game Theoretic Approach
keywords: game theory, driver model, model predictive control <br>
变道场景是值得被研究的场景之一，同时交互场景同样值得被研究,去解决变道场景中无人车交互的问题，博弈理论是一个有效的手段<br>

# 整体概览
首先，无人车被赋予了不同的驾驶风格(激进的，正常的，保守的)，为的是在决策过程中去模拟人类的驾驶行为. <br>
然后，无人车的决策制定被看作为非合作式的博弈,其中，纳什均衡以及斯坦克尔伯格博弈被用来解决决策问题.<br>
除此之外，势场法(potential field method)以及MPC被分别用来进行动作预测和规划. <br>
最后，通过不同的测试场景验证了无人车类人决策框架. <br>
整合了驾驶员模型以及车路模型的整合模型被构建. <br>
基于非合作博弈论的决策生成模块被制作. <br>
动作预测与规划模块根据势场法以及MPC被设计. <br>
# 无人车的类人决策架构图
![human-like framework](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E6%B7%B1%E5%BA%A6%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/paper/img/human-like.png) <br>
下面对架构进行详细解析 <br>
# Driver Model
单点预瞄驾驶员模型(single-point preview driver model)被引用,本文中，该模型被用于动作预测. <br>
![driver_model](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E6%B7%B1%E5%BA%A6%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/paper/img/driver_model.png) <br>
上述模型旨在通过控制无人车前轮的steering angle来最小化M点与P点的差距. <br>
