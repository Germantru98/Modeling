import numpy as np
import random
#Кол-во экспериментов
N = 1000
m = 10
delta = 0.03

def GetExperiment():
    result = 0.0
    for i in range(12):
        result +=m+delta*(random.random()-6)
    return result

def GetResult(mass):
    result=0.0
    for x in range(N):
        result+=GetExperiment()
    return result/N
        
first = []
second = []
third = []
for i in range(N):
    tmpMass = [GetExperiment(), GetExperiment(), GetExperiment()]
    tmpMass.sort()
    first.append(tmpMass[0])
    second.append(tmpMass[1])
    third.append(tmpMass[2])

print('Task1',GetResult(first))
print('Task2',GetResult(second))
print('Task3',GetResult(third))
