from cProfile import label
from turtle import color
import numpy as np
import matplotlib.pyplot as plt
a=0 
b=2

x=np.linspace(a-1,b+1,num=100)


pdf=np.where((x >= a) & (x <= b),1/(b-a),0)
cdf=np.where(
    (x >= a) & (x <= b),(x-a)/(b-a),
    np.where(x <= a,0,1))


plt.plot(x,pdf,color='b',label='fX')
plt.plot(x,cdf,color='orange',label='FX')
plt.title('Graphic representation of the uniform law X(f and F)')
plt.legend(loc='upper left')
xticks=np.arange(-1,4)
plt.xticks(xticks)
yticks=np.arange(0,1.1,step=0.25)
plt.yticks(yticks)
plt.show()
