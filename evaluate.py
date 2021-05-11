import numpy as np

def evaluate(model, env, numiter):
    policy = model(env) ##model is taken as a function, and model returns a policy function

    size = 10 #number of runs to calculate avg and std dev

    avg_reward = np.zeros(size)
    
    for i in range(size):
        reward = []
        env.reset()


        for j in range(numiter):
            state_j = env.state
            _,reward_j,_,_ = env.step(policy(state_j))
            if j >= 1000:
                reward.append(reward_j)
        
        avg_reward[i] = np.mean(reward)
    
    avg = np.mean(avg_reward)
    std_dev = np.std(avg_reward)

    print("mean: ",avg)
    print("standard deviation:", std_dev)
    
    return avg, std_dev

