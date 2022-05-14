import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw=RandomWalk()
    rw.fill_walk()
    point_numbers=list(range(rw.num_points))
    # 隐藏坐标轴
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)
    current_axes=plt.axes()
    current_axes.xaxis.set_visible(False)
    current_axes.yaxis.set_visible(False)
    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolor='none',s=15)
    plt.scatter(0,0,c='green',edgecolors='none',s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)
    plt.show()
    plt.savefig('img/11.3.8-rw_visual.png',bbox_inches='tight')
    keep_running=input("make another walk?(y/n):")
    if keep_running == 'n':
        break