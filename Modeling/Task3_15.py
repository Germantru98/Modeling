import random
import matplotlib.pyplot as plt

def GetX():
    return random.random()

n = 50

tmp = []
x = []
y = []

for i in range(n):
    tmp.append(GetX())
for j in range(n-2):
    x.append(tmp[j])
    y.append(tmp[j+2])
print('Xmass: ',x)
print('Ymass: ',y)

plt.scatter(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
