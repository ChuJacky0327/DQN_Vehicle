import matplotlib.pyplot as plt
import numpy as np
import csv


def plotLearning(x, scores, epsilons, filename, data_rate, Transmission_delay, power_consumption, lines=None):
    fig=plt.figure()
    ax=fig.add_subplot(111, label="1")
    ax2=fig.add_subplot(111, label="2", frame_on=False)

    ax.plot(x, epsilons, color="C0")
    ax.set_xlabel("Game", color="C0")
    ax.set_ylabel("Epsilon", color="C0")
    ax.tick_params(axis='x', colors="C0")
    ax.tick_params(axis='y', colors="C0")

    N = len(scores)
    running_avg = np.empty(N)
    for t in range(N):
	    running_avg[t] = np.mean(scores[max(0, t-100):(t+1)])

    ax2.plot(x, running_avg, color="C1")
    #ax2.xaxis.tick_top()
    ax2.axes.get_xaxis().set_visible(False)
    ax2.yaxis.tick_right()
    #ax2.set_xlabel('x label 2', color="C1")
    ax2.set_ylabel('Score', color="C1")
    #ax2.xaxis.set_label_position('top')
    ax2.yaxis.set_label_position('right')
    #ax2.tick_params(axis='x', colors="C1")
    ax2.tick_params(axis='y', colors="C1")

    if lines is not None:
        for line in lines:
            plt.axvline(x=line)

    plt.savefig(filename)
    
    running_avg = list(map(lambda x:[x],running_avg))
    data_rate = list(map(lambda x:[x],data_rate))
    Transmission_delay = list(map(lambda x:[x],Transmission_delay))
    power_consumption = list(map(lambda x:[x],power_consumption))
    
    with open('data/DQN_simulation1-avg_score.csv','w',newline='') as file: #'w'為覆寫
        write = csv.writer(file)
        #write.writerow(["ave_score"])
        for i in range(len(scores)):
            write.writerow(running_avg[i])
    
    with open('data/DQN_simulation1-best_data_rate.csv','w',newline='') as file: #'w'為覆寫
        write = csv.writer(file)
        #write.writerow(["ave_score"])
        for i in range(len(data_rate)):
            write.writerow(data_rate[i])
            
    with open('data/DQN_simulation1-best_Transmission_delay.csv','w',newline='') as file: #'w'為覆寫
        write = csv.writer(file)
        #write.writerow(["ave_score"])
        for i in range(len(Transmission_delay)):
            write.writerow(Transmission_delay[i])
            
    with open('data/DQN_simulation1-best_power_consumption.csv','w',newline='') as file: #'w'為覆寫
        write = csv.writer(file)
        #write.writerow(["ave_score"])
        for i in range(len(power_consumption)):
            write.writerow(power_consumption[i])
