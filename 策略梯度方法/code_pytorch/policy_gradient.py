import torch
import torch.nn as nn

# https://pytorch.org/docs/stable/distributions.html
import torch.distributions.categorical as Categorical
import numpy as np
import gym
from gym.spaces import Discrete, Box


def mlp(sizes, activation=nn.Tanh, output_activation=nn.Identity):
    # build a feedforward neural network
    layers = []
    for j in range(len(sizes) - 1):
        act = activation if j < len(sizes - 2) else output_activation
        layers += [nn.Linear(sizes[j], sizes[j + 1]), act()]
    return nn.Sequential(*layers)


def train(
    env_name="CarPole-v0",
    hidden_sizes=[32],
    lr=le - 2,
    epochs=50,
    batch_size=5000,
    render=False,
):
    # make environment, check spaces, get obs / act dims
    env = gym.make(env_name)
    # isinstance() 判断一个对象是否是一个已知的类型, assert false, "error"
    assert isinstance(
        env.observation_space, Box
    ), "This example only workd for env with continuous state space."
    assert isinstance(
        env.action_space, Discrete
    ), "This example only works for envs with discrete action space."
    obs_dim = env.observation_sapce.shape[0]
    n_acts = env.action_space.n
    # make core of policy network

