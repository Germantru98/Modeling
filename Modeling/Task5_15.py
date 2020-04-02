import math
import random
import matplotlib.pyplot as plt
import pandas as pd
l = 1
n = 1000
x = range(n)
y1 = []
y2 = []
y3 = []
def GetResult():
    return -1*((1/l)*math.log(random.random()))

def GetExp():
    result = []
    for i in range(n):
        result.append(GetResult())
    return result
#Мат ожидание до отказа  второго элемента
def Task_2():
    result = 0.0
    for i in range(n):
        firstElem = GetResult()
        secondElem = GetResult()
        if firstElem>secondElem:
            result+= firstElem
        else:
            result+= secondElem
    return result/n
#Мат ожидание до отказа всей системы
def Task_1():
    result = 0.0
    tmpMass = []
    for i in range(n):
        tmpMass = [GetResult(), GetResult(), GetResult()]
        tmpMass.sort()
        y1.append(tmpMass[0])
        y2.append(tmpMass[1])
        y3.append(tmpMass[2])
        result+=tmpMass[2]
    return result/n

print(Task_1())

#Отрисовка графика
plt.plot(x,y1,'o-r',label="Первый элемент", color = 'b')
plt.plot(x,y2,'o-r',label="Второй элемент", color = 'r')
plt.plot(x,y3,'o-r',label="Резервный элемент", color = 'g')
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()



