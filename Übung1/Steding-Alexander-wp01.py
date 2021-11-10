import numpy as np
import matplotlib.pyplot as plt
import math

#Aufgabe c)

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

plt.plot(te,mp, label="Magnus")
plt.plot(te,cp, label="Clausius-Clapperyeon")
plt.xlabel('Temperatur in °C')
plt.ylabel('Sättigungsdamfpdruck in Pa')
plt.legend( )
plt.title('Vergleich der Classiusclapereyon Gleichung und der Magnus-Formel')
plt.savefig('Steding-Alexander-wp01-plotc.png',format='png',dpi = 1200)
plt.close()

# Aufgabe e)
cppp = np.array([])
lvo= 2.5*10**6
rv = 461.4
cpv =1870
cpi= 4187
to = 273.15
for t in range(233,333):
    t = t + 0.15 #Korrektur für Temperatur
    c = 611.2*math.exp(((cpv-cpi)*(math.log(t)-math.log(to)))/(rv)+((lvo - to*(cpv-cpi))/(rv)*(((-1)/(t)+((1)/(to))))))
    cppp=np.append(cppp,c)

plt.plot(te,mp, label="Magnus")
plt.plot(te,cp, label="Clausius-Clapperyeon")
plt.plot(te,cppp, label="Clausius-Clapperyeon verbessert")
plt.legend()
plt.title('Vergleich der verbesserten CC Gleichung und der Magnus-Formel')
plt.xlabel('Temperatur in °C')
plt.ylabel('Sättigungsdamfpdruck in Pa')
plt.savefig('Steding-Alexander-wp01-plote.png',format='png',dpi = 1200)
plt.close()
#Aufgabe e) Quotient
quotientenarray= cppp/mp
plt.plot(te,quotientenarray, label="Quotient Classius/Magnus")
plt.title('Quotient der verbesserten CC Gleichung und der Magnus-Formel')
plt.legend()
plt.axis([-40,60,0.8,1.2])
plt.xlabel('Temperatur in °C')
plt.ylabel('Quotient')
plt.savefig('Steding-Alexander-wp01-plote2.png',format='png',dpi = 1200)
