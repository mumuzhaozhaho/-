import numpy
import matplotlib.pyplot as plt
import math


x=numpy.linspace(-10,10,5)#把-10到10分成100份
print(x)
y=x**2+1


plt.plot(x,y)
plt.show()