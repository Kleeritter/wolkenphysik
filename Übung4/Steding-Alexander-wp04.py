import numpy as np
import matplotlib.pyplot as plt
import math
x = np.arange (0,600,0.1)
m=1.5*10**-3
l=1000
ro= 0.2*10**(-3)
k=8*10**3
zi=[]
vo=4
koks=[]

for t in np.arange(0,600,0.1):
    u=ro*math.exp((m*k*t)/(4*l))*k
    uff= k*m*ro*math.exp((k*m*t)/(4*l))/(4*l)
    alla=vo*t -ro*math.exp((m*k*t)/(4*l))*k*t
    walla=vo*t + (ro)/(m/(4*l))*(1-math.exp((m/(4*l))*k*t))
    koks.append(walla)
a=100
b=2000
counter=0
c=7
while vo*c + (ro)/(m/(4*l))*(1-math.exp((m/(4*l))*k*c)) !=0 and counter <10000:
    c=(b+a)/2
    f=vo*c + (ro)/(m/(4*l))*(1-math.exp((m/(4*l))*k*c))
    if f>0:
        b=c
        counter +=1
    else:
        a=c
        counter +=1
print(c)
print(counter)
#plt.plot(x,koks)
#plt.axis([0,1000,-1000,1000])
#plt.show()