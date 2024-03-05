import gym
from DQN_networks_torch import Agent
from utils import plotLearning
import numpy as np

if __name__ == '__main__':
    env = gym.make('LunarLander-v2')
    agent = Agent(gamma=0.99, epsilon=1.0, batch_size=64, n_actions=4, eps_end=0.01,
                  input_dims=[8], lr=0.001)
    scores, eps_history = [], []
    n_games = 100
    
    for i in range(n_games):
        score = 0
        done = False
        observation = env.reset()
        while not done:
            action = agent.choose_action(observation)
            observation_, reward, done, info = env.step(action)
            score += reward
            agent.store_transition(observation, action, reward, 
                                    observation_, done)
            agent.learn()
            observation = observation_
        scores.append(score)
        eps_history.append(agent.epsilon)

        avg_score = np.mean(scores[-100:])

        print('episode ', i, 'score %.2f' % score,
                'average score %.2f' % avg_score,
                'epsilon %.2f' % agent.epsilon)
    filename = 'lunarlander_tf2.png' #生成的收斂圖名稱,有調整超參數的話可以改變圖的名稱比較好分辨
    figure_file = 'plots_torch/' + filename
    x = [i+1 for i in range(n_games)] #x軸,i+1=1
    plotLearning(x, score_history, eps_history, figure_file) #畫圖
