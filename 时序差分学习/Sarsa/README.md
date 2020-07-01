# Sarsa: 同轨策略(on-policy)下的时序差分控制
* 首先我们要学习动作价值函数而不是状态价值函数,对于同轨策略,我们必须对所有的状态s以及动作a估计出当前的行动策略下所有对应的q(s,a). <br>
![Sarsa](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E6%97%B6%E5%BA%8F%E5%B7%AE%E5%88%86%E5%AD%A6%E4%B9%A0/Sarsa/img/sarsa1.png) <br>
数学形式如下所示: <br>
![Sarsa](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E6%97%B6%E5%BA%8F%E5%B7%AE%E5%88%86%E5%AD%A6%E4%B9%A0/Sarsa/img/sarsa2.png) <br>
每当非终止状态St出现一次转移后,就进行上面的一次更新. 如果St+1是终止状态,那么Q(St+1,At+1)则定义为0.此更新规则用到了描述这个事件的五元组(St,At,Rt+1,St+1,At+1)中的所有元素.我们根据这五个元组把这个算法命名为:Sarsa <br>
* 对给定的策略 pi, 持续的估计其动作价值函数q_{pi},同时以q_{pi}为基础,朝着贪心优化的方向改变pi. 伪代码如下所示: <br>
![Sarsa](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E6%97%B6%E5%BA%8F%E5%B7%AE%E5%88%86%E5%AD%A6%E4%B9%A0/Sarsa/img/Sarsa3.png) <br>
