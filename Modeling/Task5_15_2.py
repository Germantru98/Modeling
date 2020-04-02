import math
import random
import matplotlib.pyplot as plt
import pandas as pd
l = 1
n = 1000
x = range(n)
y1 = []
y2 = []
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
        y1.append(firstElem)
        secondElem = GetResult()
        y2.append(secondElem)
        if firstElem>secondElem:
            result+= firstElem
        else:
            result+= secondElem
    return result/n

print(Task_2())

#Отрисовка графика
plt.plot(x,y1,'o-r',label="Первый элемент", color = 'b')
plt.plot(x,y2,'o-r',label="Второй элемент", color = 'g')
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()




