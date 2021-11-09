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

# Aufgabe e
cpp = np.array([])
lvo= 2.5*10**6
rv = 461.4
cpv =1870
cpi= 4187
to = 273.15
for t in range(233,333):
    t = t + 0.15 #Korrektur für Temperatur
    #dt= (t- 273.15) # Bestimmung von delta T
    c = 611.2*math.exp((-lvo + t*(cpv-cpi)*math.log(t)+to*(cpv-cpi))/(rv*t) -(2*to*(cpv-cpi)-lvo)/(to*rv))
    cpp=np.append(cpp,c)
print(cpp)
plt.plot(te,mp, te, cp,te,cpp)
plt.savefig('Vergleich2.png')
plt.legend()

cppp = np.array([])
lvo= 2.5*10**6
rv = 461.4
cpv =1870
cpi= 4187
to = 273.15
for t in range(233,333):
    t = t + 0.15 #Korrektur für Temperatur
    #dt= (t- 273.15) # Bestimmung von delta T
    c = 611.2*math.exp(-1*(lvo+(cpv-cpi)*(t-to))/(rv*(t+to))+(cpv-cpi)/(rv*(t+to)))
    cppp=np.append(cppp,c)
print(cppp)
plt.plot(te,mp, te, cp,te,cpp)
plt.savefig('Vergleich2.png')
plt.legend()
