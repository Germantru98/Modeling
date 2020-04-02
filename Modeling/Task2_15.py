import math
import matplotlib.pyplot as plt
#functions
def GetX(x,a):
    return a * x * x
def GetY(y,b):
    return b * y

a = 1
b = 1
h = 0.1
t = 0
xx = 1.0
yy = 1.0
x = 0.0
y = 0.0
x_array = [x]
y_array = [y]
while t < 100:
    xx = xx + h * GetX(xx,a)
    yy = yy + h * GetY(yy,b)
    x = xx
    y = yy
    x_array.append(x)
    y_array.append(y)
    t += h

plt.plot(x_array, y_array)
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
