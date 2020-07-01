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
![MC DP TD](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E6%97%B6%E5%BA%8F%E5%B7%AE%E5%88%86%E5%AD%A6%E4%B9%A0/img/dp_mc_td1.png) <br>
上图中的这颗树，代表了整个状态与动作空间。对于蒙特卡罗方法来说，要更新一次V值，需要有一个完整的样本(即图中红色部分就是一个样本)。这条路径经过了三个状态，所以可以更新三个状态的V值.由于不知道模型情况，所以无法计算从St到下面四个节点的概率以及即时奖励，所以一次只能更新一条路径. 如果重复次数够多了，就能覆盖所有的路径，最后的结果才能跟动态规划那样. <br>
![MC DP TD](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E6%97%B6%E5%BA%8F%E5%B7%AE%E5%88%86%E5%AD%A6%E4%B9%A0/img/dp_mc_td2.png) <br>
上图的红色部分是TDL每次更新所需要的.对于MC和TDL来说，它们都是模型不可知的，所以它们只能通过尝试来近似真实值. <br>
![MC DP TD](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E6%97%B6%E5%BA%8F%E5%B7%AE%E5%88%86%E5%AD%A6%E4%B9%A0/img/dp_mc_td3.png) <br>
这是动态规划的V值计算，由于知道了模型，所以可以直接计算期望V值. <br>
# TD(λ)
先前所说的TD方法实际上都是TD(0)方法.其中，0表示的是在当前状态下往前多看1步，即: <br>
Gt=Rt+1 + γV(St+1) <br>
要是往前多看2步然后再更新状态价值，那就是: <br>
Gt=Rt+1 + γRt+2 +γ^2 V(St+2) <br>
那如果是n步? <br>
# n-step TD
![n-step-TD](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E6%97%B6%E5%BA%8F%E5%B7%AE%E5%88%86%E5%AD%A6%E4%B9%A0/img/n_step_td.png) <br>
所谓的n-step TD，其实就是说要往前多少步再来估计V值.如果往前n步直到终点，那么就等价于蒙特卡罗方法了. <br>
![n-step-TD](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E6%97%B6%E5%BA%8F%E5%B7%AE%E5%88%86%E5%AD%A6%E4%B9%A0/img/n_step_td1.png) <br>
选择多少步数n作为一个较优的计算参数也是一个问题.于是，引入一个新的参数 λ.通过这个新的参数，可以做到在不增加计算复杂度的情况下综合考虑所有步数的预测. <br>
![n-step-TD](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E6%97%B6%E5%BA%8F%E5%B7%AE%E5%88%86%E5%AD%A6%E4%B9%A0/img/n_step_td2.png) <br>
从上图中的定义可以看出，这是综合了所有步数的情况，我们不直接选取一个具体的n步，然后忽略掉其它的步数.而是利用λ来综合所有的步. <br>
给出这样的定义，有点像之前的γ参数一样，是用来控制权重的.而这里的λ的形式就是这样，它的权重就是下图所示: <br>
![n-step-TD](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E6%97%B6%E5%BA%8F%E5%B7%AE%E5%88%86%E5%AD%A6%E4%B9%A0/img/n_step_td3.png) <br>
经过这个$(1−λ)λ^{n−1}$的作用，各个步数的权重就像上图这样衰减.相当于离状态s越远的，权重就越小。这也符合我们一般的想法，离得远的作用就小. <br>
# 前向TD(λ)
引入λ之后，会发现要更新一个状态的价值，必须要有一个完整的episode(看前面的公式)。这和MC算法的要求一样。所以前向TD(λ)在实际应用中也很少. <br>
![前向TD](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E6%97%B6%E5%BA%8F%E5%B7%AE%E5%88%86%E5%AD%A6%E4%B9%A0/img/forward_td.png) <br>
前向视角的解释：假设一个人坐在状态流上拿着望远镜看向前方，前方是那些将来的状态. 当估计当前状态的值函数时，从TD(λ)的定义中可以看到，它需要用到将来时刻的值函数. <br>
![前向TD](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E6%97%B6%E5%BA%8F%E5%B7%AE%E5%88%86%E5%AD%A6%E4%B9%A0/img/forward_td1.png) <br>

# 后向TD(λ)
![后向TD](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E6%97%B6%E5%BA%8F%E5%B7%AE%E5%88%86%E5%AD%A6%E4%B9%A0/img/behind_td.png) <br>
TD(λ)的后向视角解释：有个人坐在状态流上，手里拿着话筒，面朝着已经经历过的状态，获得当前回报并利用下一个状态的值函数得到TD偏差之后，此人会想已经经历过的状态喊话告诉这些已经经历过的状态处的值函数需要利用当前时刻的TD偏差进行更新. 此时过往的每个状态值函数更新的大小应该跟距离当前状态的步数有关. 假设当前状态为st，TD偏差为δt，那么St−1处的值函数更新应该乘以一个衰减因子γλ，状态St−2处的值函数更新应该乘以(γλ)^2，以此类推. <br>
![后向TD](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E6%97%B6%E5%BA%8F%E5%B7%AE%E5%88%86%E5%AD%A6%E4%B9%A0/img/behind_td1.png) <br>
对状态空间中的每一个状态s，更新价值函数. <br>
(注意这里是对已经经历过的所有状态都更新v值) <br>
参考自: https://blog.csdn.net/liweibin1994/article/details/79111536 <br>
