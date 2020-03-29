import math
import matplotlib.pyplot as plt
#functions
def GetR(x,y):
	return math.pow(math.sqrt(x * x + y * y),3)
def GetX(k,x,r):
    return -1 * (k * x) / (r * m)
def GetY(k,y,r):
    return -1 * (k * y) / (r * m)
#Масса чаcтицы
m = 0.001
#Постоянная Больцмана
k = 0.014
#Др.  переменные
h = 0.1
n = 0
x = 1.0
y = 1.0
x_1 = 0
y_1 = 0
x_array = [x]
y_array = [y]
while n < 1000:
    x_1 = x_1 + h * GetX(k,x,GetR(x,y))
    y_1 = y_1 + h * GetY(k,y,GetR(x,y))
    x = x_1
    y = y_1
    x_array.append(x)
    y_array.append(y)
    n += h

plt.plot(x_array, y_array)
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
