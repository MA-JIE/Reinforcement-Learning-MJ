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
为了避免在真实环境中很难被满足的试探性出发假设，
