# 时序差分学习
TD learning的特点: <br>
* TD methods learn directly from episodes of experience <br>
* TD is model-free: no knowledge of MDP transitions / rewards <br>
* TD learn from incomplete episodes by bootstrapping <br>
* TD updates a guess towards a guess <br>
TD Learning中才会把Gt写成递归的形式。这样，每走一步都可以更新一次V。而蒙特卡罗中，却需要走完整个样本，才能得到Gt，从而更新一次.蒙特卡罗学习方法的更新是这样的: <br>
V(St) <-- V(St) + alpha (Gt - V(St)) <br>
在TD learning中，算法在估计某一个状态的价值时，用的是离开该状态时的即时奖励Rt+1与下一个状态St+1的预估状态价值乘以折扣因子γ组成. <br>
