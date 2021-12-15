import matplotlib.pyplot as plt
import math

def sigma(x):
    ret = 0
    c = []
    for val in x:
       ret += val
       c.append(ret)
    return c


b = []
for i in range(1,1000):
        b.append(i/100*100*(1/10))
d = sigma(b)
print(d)
a = []
for i in range(len(b)):
    a.append(i)
print(a)
plt.plot(a,b)
plt.ylim(0,d[-1])
plt.xlim(0,a[-1])
plt.show()