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

