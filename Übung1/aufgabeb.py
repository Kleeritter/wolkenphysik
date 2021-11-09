import numpy as np
import matplotlib.pyplot as plt
import math
alas = np.arange(0,10,1)
blas= np.arange(10,20,1)

te= np.arange(-40,60,1)

#Magnusformel
mp = np.array([])
for t in range(-40,60):
    m=611.2 * math.exp((17.62*t)/(243.12+t))
    mp=np.append(mp, m)



#Clausiusclaperyon
cp = np.array([])
lv= 2.5*10**6
rv = 461.4
for t in range(233,333):
    t = t + 0.15 #Korrektur für Temperatur
    dt= (t- 273.15) # Bestimmung von delta T
    c = 611.2*math.exp((lv*dt)/(rv*t*273.15))
    cp=np.append(cp,c)

plt.plot(te,mp, te, cp)
plt.savefig('Vergleich.png')
plt.legend()


Hw = 7 