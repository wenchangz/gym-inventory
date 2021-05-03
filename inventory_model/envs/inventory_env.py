import gym
import numpy as np
import sys

class Inventory(gym.Env):
    metadata = {'render.modes': ['human']}
    
    #def __init__(self, config): 
    def __init__(self): 
        
#         self.h = config['h'] # the holding cost
#         self.p = config['p'] # the penalty cost
#         self.L = config['L'] # leading time
#         self.N = config['max_inventory'] # maximum inventory
#         self.D = config['max_demand'] # maximum demand
        #self.starting_state = config['starting_state'] # set initial state
        
        self.h = 1 # the holding cost
        self.p = 2 # the penalty cost
        self.L = 100 # leading time
        self.N = 100 # maximum inventory
        self.D = 6 # maximum demand
        

        self.action_space = gym.spaces.Discrete(self.N+1) # definition of the action space
        self.observation_space = gym.spaces.MultiDiscrete([self.N+1]*(self.L+1)) # definition of the state space
        
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
        
        demand = np.random.binomial(self.D, 0.5)
        
        # update inventory
        self.state[0] = min(self.N, max(0, self.state[0] + self.state[1] - demand))
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
       