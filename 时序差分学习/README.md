# 时序差分学习
TD learning的特点: <br>
* TD methods learn directly from episodes of experience <br>
* TD is model-free: no knowledge of MDP transitions / rewards <br>
* TD learn from incomplete episodes by bootstrapping <br>
* TD updates a guess towards a guess <br>
TD Learning中才会把Gt写成递归的形式。这样，每走一步都可以更新一次V。而蒙特卡罗中，却需要走完整个样本，才能得到Gt，从而更新一次.蒙特卡罗学习方法的更新是这样的: <br>
V(St) <-- V(St) + alpha (Gt - V(St)) <br>
在TD learning中，算法在估计某一个状态的价值时，用的是离开该状态时的即时奖励Rt+1与下一个状态St+1的预估状态价值乘以折扣因子γ组成: <br>
* Update value V(St) toward estimated return Rt+1 + γV(St+1) <br>
V(St) <-- V(St) + alpha (Rt+1 + γV(St+1)  - V(St)) <br>
* Rt+1 + γV(St+1) is called the TD target <br>
* Rt+1 + γV(St+1)  - V(St) is called TD error <br>
其中，bootstrapping指的就是TD目标值 Rt+1+γV(St+1) 代替Gt的过程.显然，蒙特卡罗每次更新都需要等到agent到达终点之后再更新;而对于TD learning来说，agent每走一步它都可以更新一次，不需要等到到达终点之后才进行更新. <br>
示例: <br>
![MC VS TD](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E6%97%B6%E5%BA%8F%E5%B7%AE%E5%88%86%E5%AD%A6%E4%B9%A0/img/mc_td.png) <br>
假如应用MC算法，由于需要完整的episode，因此，只有episode 1 能够用来计算A的状态值，所以显然，V(A) = 0；同时B状态的价值为6/8。而对于TD算法来说，由于状态A的后继有状态B，所以状态A的价值是通过状态B的价值来计算的。所以根据上面TD的计算公式，V(A)=V(B) = 6/8. <br>
# MC TDL DP
Monte-Carlo, Temporal-Difference 和Dynamic Programming这三种学习方法都是用来计算状态价值的. 它们的区别在于，前两种是在不知道模型的情况下常用的方法，而MC方法又需要一个完整的episode来更新状态价值，TD则不需要完整的episode. DP方法则是基于Model(知道模型的运作方式)的计算状态价值的方法. 它通过计算一个状态S所有可能的转移状态S’及其转移概率以及对应的即时奖励来计算这个状态S的价值。也正是因为它知道整个模型的情况(知道状态转移概率与即时奖励)，所以它才能够这样子计算全面的情况. 下面的图可以直观地看出它们的区别: <br>
![MC DP TD](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E6%97%B6%E5%BA%8F%E5%B7%AE%E5%88%86%E5%AD%A6%E4%B9%A0/img/.png) <br>
