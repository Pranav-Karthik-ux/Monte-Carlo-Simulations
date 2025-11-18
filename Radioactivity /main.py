import random as rn
import numpy as np
from matplotlib import pyplot as plt
def random_array(N):
    f=np.zeros(N)
    for i in range(N):
        f[i]=rn.random()
    return f       
def monte_carlo(N0,D0,p,tmax):
    N1=N0
    D1=D0
    f=[]
    k=[]
    t=0
    t1=[]
    dt=0.5
    while N1>0 and t<tmax:
        M=random_array(N1)
        f.append(N1)
        k.append(D1)
        t=t+dt
        t1.append(t)

        for i in range(N1):
            if M[i]<=p:
                N1-=1
                D1+=1
        
    return f,k,t1
A,B,T= monte_carlo(1000,0,0.2,15)
print(A,B,T)
plt.plot(T,A,'o-')
plt.xlabel('time')
plt.ylabel('No of Nucleon')
plt.show()
