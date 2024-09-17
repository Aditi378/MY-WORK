import matplotlib.pyplot as plt
import numpy as np
'''
#subplot 1
x=np.array([1,2,3,4,5])
y=np.array([4,6,4,8,1])
plt.subplot(2,3,1)
plt.xlabel("plot1x")
plt.ylabel("plot1y")
plt.title("plot 1")
plt.grid()
plt.plot(x,y)

#subplot 2
x=np.array([0,4,5,6,7])
y=np.array([0,3,4,5,7])
plt.subplot(2,3,2)
plt.xlabel("plot2x")
plt.ylabel("plot2y")
plt.title("plot 2")
plt.grid()
plt.plot(x,y)

#subplot 3
x=np.array([0,1,5,6,7])
y=np.array([11,22,33,44,55])
plt.subplot(2,3,3,)
plt.xlabel("plot3x")
plt.ylabel("plot3y")
plt.title("plot 3")
plt.grid()
plt.plot(x,y)

#subplot 4
x=np.array([10,20,30,40,50])
y=np.array([66,77,88,99,100])
plt.subplot(2,3,4)
plt.xlabel("plot4x")
plt.ylabel("plot4y")
plt.title("plot 4")
plt.grid()
plt.plot(x,y)

#subplot 5
x=np.array([0,9,8,7,6])
y=np.array([0,3,6,3,9])
plt.subplot(2,3,5)
plt.xlabel("plot5x")
plt.ylabel("plot5y")
plt.title("plot 5")
plt.grid()
plt.plot(x,y)
'''
#subplot 6
x=np.array([0,88,44,55,99])
y=np.array([23,24,25,26,27])
plt.subplot(2,3,6)
plt.grid()
plt.xlabel("plot6x")
plt.ylabel("plot6y")
plt.title("plot 6")
plt.grid()
plt.scatter(x,y)

plt.suptitle("6 graph subplotss")
plt.show()