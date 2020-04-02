import numpy as np
import random
import matplotlib.pyplot as plt
#Кол-во экспериментов
N = 1000
m = 10
delta = 0.03
x = range(N)
y1 = []
y2 = []
y3 = []
def GetExperiment():
    result = 0.0
    for i in range(12):
        result +=m + delta * (random.random() - 6)
    return result

def GetResults():
    for i in range(N):
         tmpMass = [GetExperiment(), GetExperiment(), GetExperiment()]
         tmpMass.sort()
         y1.append(tmpMass[0])
         y2.append(tmpMass[1])
         y3.append(tmpMass[2])

def Task(mass):
    result = 0.0
    for item in mass:
        result+=item
    return result/N
       
GetResults()
print('Task1',Task(y1))
print('Task2',Task(y2))
print('Task3',Task(y3))

#Отрисовка графика
plt.plot(x,y1,'o-r',label="Первый элемент", color = 'b')
plt.plot(x,y2,'o-r',label="Второй элемент", color = 'r')
plt.plot(x,y3,'o-r',label="Третий элемент", color = 'g')
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
