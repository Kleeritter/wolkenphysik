import numpy as np
import matplotlib.pyplot as plt
import math

#a Köhlerkurve
rad= np.arange(1*10**(-9),100*10**(-6),1*10**(-9))
amo= np.array([])
seesalzschwer= np.array([])
seesalzleicht=np.array([])
T=273.15
A= T**(-1) *3.3*10**(-7)

#Ammoniunmsulfat
for r in  np.arange(1*10**(-9),100*10**(-6),1*10**(-9)):
    v=3
    masse=10**(-19)
    molmasse=  0.13214
    B= (v*masse*molmasse**(-1))*4.3*10**(-6)
    s= 1+ (A/r) -(B/(r**3))
    amo=np.append(amo,s)

#Seesalzschwer
for r in  np.arange(1*10**(-9),100*10**(-6),1*10**(-9)):
    v=2
    masse=10**(-19)
    molmasse=  0.05844 
    B= v*masse*molmasse**(-1)*4.3*10**(-6)
    s= 1+ (A/r) -(B/(r**3))
    seesalzschwer=np.append(seesalzschwer,s)

#Seesalzleicht
for r in  np.arange(1*10**(-9),100*10**(-6),1*10**(-9)):
    v=2
    masse=10**(-21)
    molmasse=  0.05844 
    B= v*masse*molmasse**(-1)*4.3*10**(-6)
    s= 1+ (A/r) -(B/(r**3))
    seesalzleicht=np.append(seesalzleicht,s)


plt.plot(rad,amo,label="Amoniumsulfat")
plt.plot(rad,seesalzschwer,label="Seesalz schwer")
plt.plot(rad,seesalzleicht,label="Seesalz leicht")
plt.axis([10**-9,10**-4,0.98,1.05])
plt.xscale("log")
plt.legend()
plt.savefig("test.png",dpi=600)