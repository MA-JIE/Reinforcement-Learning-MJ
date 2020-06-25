蒙特卡洛方法
==========
在马尔科夫决策过程(MDP)，MDP是通过5元组：<S,P,A,R,γ>来做决策的。对于这种已知模型的情况，我们可以容易获得奖赏最大化。但是，在现实世界中，我们无法同时知道这个5元组。比如P，状态转移概率就很难知道，P不知道，我们就无法使用bellman方程来求解V和Q值。<br>
但是我们依然要去解决这个问题，当我们不拥有完备的环境知识模型时，我们无法用基于模型的策略迭代或价值迭代的方式去真正地计算每个状态的值函数。<br>
对于蒙特卡洛算法，我们需要的是经验，即从真实或者模拟的环境中交互采样得到状态，动作，收益的序列。该算法通过平均样本的回报来解决强化学习问题。<br>
在分幕式的任务中，比如：下一盘棋，对于价值估计以及策略改进我们将在整个幕结束时才进行，即逐幕做出改进，并非在线改进。<br>

# 蒙特卡洛预测
假设策略pi下途径状态s的多幕数据，我们想要估计策略pi下状态s的价值函数。<br>
* 首次访问型ＭＣ算法:<br>
用s的所有首次访问的回报的平均值估计价值函数。伪代码如下图所示:<br>
![first_visit](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E8%92%99%E7%89%B9%E5%8D%A1%E6%B4%9B%E6%96%B9%E6%B3%95/img/first_visit.png) <br>
假设下图为一个分幕式的动作:<br>
![mc_prediction](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E8%92%99%E7%89%B9%E5%8D%A1%E6%B4%9B%E6%96%B9%E6%B3%95/img/mc_prediction.png)  <br>
第一幕中，状态s第一出现时的累计回报Ｇ11 = +2, 第二次出现时的Ｇ12 = 0+1-3+5　= +3 <br>
![mc_prediction2](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E8%92%99%E7%89%B9%E5%8D%A1%E6%B4%9B%E6%96%B9%E6%B3%95/img/mc_prediction2.png) <br>
假设状态s统计的次数为Ｎ(S)，那么状态s的价值函数为:<br>
ｖ(s) = (G11 + G21 + ....) / N(S) <br>
``` python
pi = init_pi()
returns = defaultdict(list)
for i in range(NUM_ITER):
    episode = generate_episode(pi) # (1)
    G = np.zeros(|S|)
    prev_reward = 0
    for (state, reward) in reversed(episode):
        reward += GAMMA * prev_reward
        # backing up replaces s eventually,
        # so we get first-visit reward.
        G[s] = reward
        prev_reward = reward
    for state in STATES:
        returns[state].append(state)
V = { state : np.mean(ret) for state, ret in returns.items() }
```
* 每次访问型ＭＣ算法:<br>
使用所有访问的回报的平均值估计价值函数。<br>
假设状态s出现的所有的次数为Ｎ(S)，那么状态s的价值函数为:<br>
ｖ(s) = (G11 + G12 + G21 + G22 + ....) / N(S) <br>
* MC算法的一个重要事实是:<br>
对于每个状态的估计是独立的，它对于一个状态下的估计完全不依赖于对其他状态的估计。当我们仅仅需要获得某个状态s而不是所有状态的价值函数或者某个子集状态的价值函数时可以使用MC算法。<br>

# 动作价值的蒙特卡洛估计
如果无法得到环境的模型，计算状态-动作价值函数更加有用些，我们必须显示地确定每个动作的价值函数来确定一个策略。同样也可以分为每次访问型或者首次访问型<br>
但是，如果pi是一个确定性的策略，一些“状态－动作”对可能永远不会被访问到，那么MC算法将无法根据经验改善动作价值函数的估计。<br>
* 试探性假设:<br>
一种方法是将指定的“状态－动作”组作为起点开始一幕采样，同时保证所有的“状态－动作”二元组都有非另的概率可以被选为起点。这样经过一定次数的幕，我们可以得出每个二元组的回报均值了。<br>
# 蒙特卡洛控制
通过上述基于试探性假设的动作价值的蒙特卡洛估计，我们可以求解出初始策略pi下的状态-动作值函数，然后我们就可以进行策略迭代了。<br>
![mc_control](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E8%92%99%E7%89%B9%E5%8D%A1%E6%B4%9B%E6%96%B9%E6%B3%95/img/mc_control.png)<br>
策略评估==>策略改进,经过多次迭代后，近似的动作价值函数会逐渐地趋向真实的动作价值函数。<br>
策略改进的方法还是在当前的价值函数上贪心地选择动作:<br>
![mc_tanxin](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E8%92%99%E7%89%B9%E5%8D%A1%E6%B4%9B%E6%96%B9%E6%B3%95/img/tanxin.png)<br>
上述算法基于两个很强的假设:(1)试探性出发的假设。　(2)策略评估时有无限多幕的样本系列进行试探。<br>
* 试探性出发的蒙特卡洛(蒙特卡洛ES)<br>
对于蒙特卡洛策略迭代，自然可以逐幕交替进行评估与改进，而不是像之前每次策略评估都要经过无限多幕。每一幕结束后，使用观测得到的回报进行策略评估，然后在该墓序列访问到的每一个状态上进行策略的改进，该算法与基于完备模型的动态规划过程思路一样。<br>
知乎中这样解释:<br>
面对这么大一个搜索空间，一个补救方法是假定我们每个幕都会从一个特定的状态开始，并采取特定的行动，也就是试探性出发，然后从所有可能回报中抽样。它背后的思想是认定我们能从任意状态开始，并在每个幕之初采取所有动作，同时策略评估过程可以利用无限幕完成。这在很多情况下是不合常理的，但在环境未知问题中却有奇效。<br>
伪代码如下:<br>
![mc_es](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E8%92%99%E7%89%B9%E5%8D%A1%E6%B4%9B%E6%96%B9%E6%B3%95/img/mc_es.png)<br>

# 无试探性出发的蒙特卡洛控制
为了避免在真实环境中很难被满足的试探性出发假设，唯一的一般性解决方案就是智能体能够持续不断地选择所有可能的动作，有两种方法可以保证这一点，分别成为:<br>
* 同轨策略(on policy):ϵ-Greedy策略<br>
用于生成采样数据序列的策略和用于实际决策的待评估和改进的策略是相同的，即评估、优化现在正在做决策的那个策略。<br>
ϵ-Greedy策略:<br>
因为我们要“不再贪婪”，最简单的方法就是用ε-greedy：对于任何时刻t的执行“探索”小概率 ，我们会有ϵ < 1的概率会随机选择一个动作，相比贪婪策略，ϵ-Greedy随机选择策略（不贪婪）的概率是 ϵ / |A(s)|, 选中贪心动作的概率为 1 - ϵ - ϵ / |A(s)|。<br>
伪代码如下:<br>
![on_policy](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E8%92%99%E7%89%B9%E5%8D%A1%E6%B4%9B%E6%96%B9%E6%B3%95/img/on_policy.png)<br>
* 离轨策略(off policy)<br>
用于生成采样数据序列的策略和用于实际决策的待评估和改进的策略是不相同的，即改进的则是和现在正在做决策的那个策略不同的策略。<br>

# 基于重要度采样的离轨策略
* pi 目标策略: 我们希望能优化这些策略已获得最高回报,即用来学习的策略.<br>
* b  动作策略: 我们正在用b生成π之后会用到的各种数据，即用于生成行动样本的策略. <br>
Off-policy策略通常涉及多个agent，其中一个agent一直在生成另一个agent试图优化的数据，我们分别称它们为动作策略和目标策略。就像神经网络比线性模型更“有趣”，同样的，Off-policy策略一般也比On-Policy策略更好玩，也更强大。当然，它也更容易出现高方差，更难收敛。<br>
重要性采样则是统计学中估计某一分布性质时使用的一种方法。它在这里充当的角色是回答“给定 Eb[G]，Epi[G]是什么”？换句话说，就是我们如何使用从 b 抽样得到的信息来确定 pi 的预期回报？<br>
直观来看，如果 b 选了很多 a， pi 也选了很多 a ，那 b 在 pi 中应该发挥着重要作用；相反地，如果 b 选了很多 a， pi 并不总是跟着 b 选 a，那 b 因 a 产生的状态不会对 pi 因 a 产生的状态产生过大影响。<br>
重要度采样比:对回报值根据其轨迹在目标策略与行动策略中出现的相对概率进行加权．<br>
给定起始状态Ｓt,后续的状态－动作轨迹Ａt,St+1,At+1,,,,,,ST在策略pi下发生的概率为:<br>
![采样比](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E8%92%99%E7%89%B9%E5%8D%A1%E6%B4%9B%E6%96%B9%E6%B3%95/img/sampling.png)<br>
![采样比](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E8%92%99%E7%89%B9%E5%8D%A1%E6%B4%9B%E6%96%B9%E6%B3%95/img/caiyangbi.png)<br>
* 一般重要性采样
* 加权重要性采样
# 增量式实现
蒙特卡洛预测方法也可以采用增量式的实现方式，假设我们使用上节中的加权重要性采样，我们有一个回报序列G1,G2,....,Gn-1,他们都从相同的状态开始，且每一个回报都对应一个随机权重Wi,那么我们可以得到如下形式的一些抽样算法：<br>
![增量式实现](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E8%92%99%E7%89%B9%E5%8D%A1%E6%B4%9B%E6%96%B9%E6%B3%95/img/incremental.png)<br>
我们为了能不断跟踪Vn的变化，必须为每一个状态维护前n个回报对应的权值的累加和Ｃn.Vn的更新方法为:<br>
![增量式实现](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E8%92%99%E7%89%B9%E5%8D%A1%E6%B4%9B%E6%96%B9%E6%B3%95/img/incremental1.png)<br>
# 离轨策略的蒙特卡洛控制
![增量式实现](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E8%92%99%E7%89%B9%E5%8D%A1%E6%B4%9B%E6%96%B9%E6%B3%95/img/incremental２.png)<br>
