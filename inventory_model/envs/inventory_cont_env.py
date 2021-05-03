import gym
import numpy as np
import sys

class ContInventory(gym.Env):
    metadata = {'render.modes': ['human']}
    
    #def __init__(self, config): 
    def __init__(self): 
        
#         self.h = config['h'] # the holding cost
#         self.p = config['p'] # the penalty cost
#         self.L = config['L'] # leading time
#         self.lamb = config['lambda'] # demand rate
        #self.starting_state = config['starting_state'] # set initial state
        
        self.h = 1 # the holding cost
        self.p = 1 # the penalty cost
        self.L = 100 # leading time
        self.lamb = 1 # demand rate
        
        self.action_space = gym.spaces.Box(low=0, high=np.inf, shape=(1,1),dtype=np.float32) # definition of the action space
        self.observation_space = gym.spaces.Box(low=0, high=np.inf, shape=(self.L+1,1), dtype=np.float32) # definition of the state space
        
        #self.state = np.asarray(self.starting_state) 
        self.state = np.array([0]*(self.L+1)) 

        self.seed()


    def seed(self, seed=None):
        self.np_random, seed = gym.utils.seeding.np_random(seed)
        return [seed]

   
    def reset(self):
        #self.state = np.asarray(self.starting_state)
        self.state = np.array([0]*(self.L+1)) 
        return self.state
    
    
    def step(self, action):
        assert self.action_space.contains(action)
        
        demand = np.random.exponential(self.lamb,1)
        
        # update inventory
        self.state[0] = max(0, self.state[0] + self.state[1] - demand)
        #total inventory no more than N: this may lead to some problems with holding cost?

        # update pipeline vector x
        for i in range(1,self.L):
            self.state[i] = self.state[i+1]
        self.state[self.L] = action
        
        # compute the reward
        loss = -min(0, self.state[0] + self.state[1] - demand)
        reward = -self.h*self.state[0] - self.p*loss

        return self.state, reward, False, {}
    
#     def render(self , mode=’human’):
#         outfile = sys.stdout if mode == ’human’ else super(Inventory , self).render(mode=mode)
#         outfile.write(np.array2string(self.state)+'\n')
       