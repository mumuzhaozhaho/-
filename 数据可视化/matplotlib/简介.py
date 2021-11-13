import matplotlib.pyplot as plt
#matplotlib.pyplot是绘制各种可视化图形的命令子库，相当与快捷方式
plt.plot([1,5,9],[6,10,23])
#plt.axis()  x轴和y轴坐标
plt.axis([0,10,5,30])
plt.show()
plt.plot([5,10,6,4,2])   #当仅有一个维度时，横坐标为索引
plt.ylabel('age')
#plt.savefig('age',dpi=600) #保存文件
plt.show()

