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
T_p: driver's predicted time <br>
v_x: the longitudinal velocity of the vehicle <br>
Y and Y_p are the lateral coordinate position of the vehicle and preview point <br>
最终，M，P的距离与前轮转向角的关系可描述为: <br>
![driver_model](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E6%B7%B1%E5%BA%A6%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/paper/img/driver_model1.png) <br>
# Vehicle-Road Model
引入自行车模型，描述了全局坐标系下的自行车模型.<br>

# Integrated Model for Human-like Driving
将driver-model与Vehicle-model进行整合，用于动作预测: <br>
![integrated_model](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E6%B7%B1%E5%BA%A6%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/paper/img/integrated_model.png) <br>
a_x:自行车模型输入 <br>
Y_p:驾驶员模型输入 <br>
输出：车辆状态和位置 ,被用于决策以及motion planning <br>

# 基于非合作博弈论的决策生成
前提:障碍物车辆只进行加速，加速，无变道动作.<br>
#### Modeling for Lane-change Decision Making
![lane_change](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E6%B7%B1%E5%BA%A6%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/paper/img/lane_change.png) <br>
对于上述场景，无人车前方车辆低速行驶，无人车将会决定左变道还是右变道，或者跟随前方车辆直线行驶.<br>
驾驶安全性，舒适性，通行效率将会被考虑,加上权重系数整合为cost function <br>
drive safety cost:由纵向安全cost以及横向安全cost组成.<br>
ride comfort: 直接与横纵向加速度相关. <br>
the travel efficiency: 与无人车的纵向速度有关. <br>
以上为无人车自身的cost函数计算方式，对于障碍物车辆的cost function计算方式类似，不同的是障碍物车辆不需要考虑左右变道,比如:障碍物车辆的ride comfort cost只和纵向加速度相关.<br> 
之前提到的三种驾驶风格: aggressive, normal and conservative用来描述无人车的驾驶行为，不同驾驶风格之间的差异体现在上述cost function加权系数的不同设置上,分别对应travel efficiency，ride comfort，drive safety,不同风格对应的权重系数设置如下:<br>
![lane_change](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E6%B7%B1%E5%BA%A6%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/paper/img/driving_style.png) <br>
#### Noncooperative Decision Making Based on Nash Equilibrium
无人车与主车被认为是相互独立的 <br>
#### Noncooperative Decision Making Based on Stackelberg Equilibrium
相邻障碍物车辆与主车的行为决策将会相互影响. <br>
# MOTION PREDICTION AND PLANNING BASED ON THE POTENTIAL FIELD MODEL METHOD AND MPC


