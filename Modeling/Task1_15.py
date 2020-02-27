import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math


#Функция описывающая поведение биомассы
def func(M,  m,  K,  S, eps):
    return (m * M * S) / (K + S) - eps * M

df = pd.DataFrame({'t': [0],'M': [0]})
#Переменные
T = 3
m = 1
K = 1
S = 1
eps = -1
M = 100
t = 0
h = 0.1
i=0
#Основной цикл
while t < T:
      M = func(M, m, K, S, eps)
      df.loc[i] = [t,M]
      i = i + 1
      t+=h
print(df)


#Отрисовка графика
plt.plot(df["t"], df["M"], color = 'blue')
plt.xlabel("t")
plt.ylabel("M")
plt.show()
