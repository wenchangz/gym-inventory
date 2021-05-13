import numpy as np

def ppo_evaluate(model, env, numiter):

    size = 5 #number of runs to calculate avg and std dev

    avg_reward = np.zeros(size)
    
    for i in range(size):
        reward = np.zeros(numiter)
        obs = env.reset()

        for j in range(numiter):
            action, _states = model.predict(obs)
            obs, rewards, dones, info = env.step(action)
            reward[j] = rewards
        
        avg_reward[i] = np.mean(reward)
    
    avg = np.mean(avg_reward)
    std_dev = np.std(avg_reward)

    print("mean: ",avg)
    print("standard deviation:", std_dev)
    
    return avg, std_dev