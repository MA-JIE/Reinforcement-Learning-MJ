# Q-learning(离轨策略下的时序差分控制)
该算法的提出是强化学习早期的一个重要突破.其定义如下: <br>
![Q](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E6%97%B6%E5%BA%8F%E5%B7%AE%E5%88%86%E5%AD%A6%E4%B9%A0/Q-learning/img/Q_learning.png) <br>
待学习的动作价值函数Q采用了对最优动作价值函数q*的直接近似学习目标,而与用于生成智能体决策序列轨迹的行动策略pi是什么无关, 而Sarsa的学习目标中使用的是待学习的动作价值函数本身,由于他的计算需要知道下一时刻的动作At+1,因此与生成数据的行动策略是相关的.<br>
Q-learning的收敛性也已经被证明,其学习流程如下所示: <br>
![Q](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E6%97%B6%E5%BA%8F%E5%B7%AE%E5%88%86%E5%AD%A6%E4%B9%A0/Q-learning/img/Q-learning1.png) <br>
## 相关博客
http://mnemstudio.org/path-finding-q-learning-tutorial.htm <br>
通过手算的方式可以更好地帮助我们理解Q-Learning算法的原理. <br>
