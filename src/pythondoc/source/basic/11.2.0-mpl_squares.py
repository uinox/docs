import matplotlib.pyplot as plt

squares = [1,4,9,16,25]
plt.plot(squares)
# 打开matplotlib查看器，并 显示绘制的图形
plt.show()
# 保存为图片
plt.savefig('img/11.2.0-squares.png',bbox_inches='tight')