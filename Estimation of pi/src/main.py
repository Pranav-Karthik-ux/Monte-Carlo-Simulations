import random as rn
from matplotlib import pyplot as plt 

def pi_cal(ns):
    nc=0
    for i in range(ns):
        x=rn.random()
        y=rn.random()
        if x**2+y**2<1:
            nc+=1
    return 4*nc/ns
print(pi_cal(200))
