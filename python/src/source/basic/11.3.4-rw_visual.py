import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw=RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values,rw.y_values,s=15)
    plt.show()
    plt.savefig('img/11.3.4-rw_visual.png',bbox_inches='tight')
    keep_running=input("make another walk?(y/n):")
    if keep_running == 'n':
        break