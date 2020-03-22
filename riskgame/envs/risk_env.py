import gym
from gym import spaces

class RiskEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    
    def __init__(self):
        super().__init__()
        print('Initializing risk!')
    
    def step(self, action):
        print(action)
    
    def reset(self):
        pass

    def render(self, mode='human'):
        print('Rendering', mode)

    def close(self):
        # not used
        pass