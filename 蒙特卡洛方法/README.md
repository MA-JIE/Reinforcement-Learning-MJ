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
第一幕中，状态s第一出现时的累计回报Ｇ11 = +2, 第二次出现时的Ｇ12 = 0+1-3+5　= +3
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

