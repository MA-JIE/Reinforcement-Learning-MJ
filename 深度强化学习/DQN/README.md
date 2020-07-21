# DQN
pytorch官网有QON算法详解以及代码实现: <br>
https://pytorch.org/tutorials/intermediate/reinforcement_q_learning.html <br>
中文文档: <br>
https://pytorch.apachecn.org/docs/1.0/reinforcement_q_learning.html <br>
# 算法框架图
![DQN](https://github.com/MA-JIE/Reinforcement-Learning-MJ/blob/master/%E6%B7%B1%E5%BA%A6%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/DQN/img/DQN.jpg) <br>
Actions are chosen either randomly or based on a policy, getting the next step sample from the gym environment. We record the results in the replay memory and also run optimization step on every iteration. Optimization picks a random batch from the replay memory to do training of the new policy. “Older” target_net is also used in optimization to compute the expected Q values; it is updated occasionally to keep it current. <br>
