##############################################################################
########################################################## necessary modules #
##############################################################################
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

##############################################################################
############################################################### computations #
##############################################################################

#------------------------------------------------------define basic parameters
radien=np.loadtxt("wp_03_data.txt")
r_min= min(radien)#1e-8
r_max= max(radien)
n_bins= 1000     
phi =  n_bins/(math.log10(r_max/r_min)) #hier keine Zahl, sondern eine Berechung mit obigen Parametern einfuegen!

# A Begin

file = open('wp_03_data.txt','r')

n_data = 0
r_data = []

for line in file:
    r_data.append(float(line))
    n_data = n_data + 1

# A End

# B Begin

rl = []
rr = []
rc = []
dr = []
co = []

for i in np.arange(n_bins+2):
    rl.append(r_min*10**(i/phi))
    
for j in np.arange(n_bins+1):
    rr.append(rl[j+1]) 
    dr.append(rr[j]-rl[j]) 
    rc.append((rl[j]+dr[j]/2)) 
    co.append(0)

# B End   

# C Begin
for k in np.arange(n_data):
    for l in np.arange(n_bins):
        if rl[l] <= r_data[k] and r_data[k] < rr[l]:
            co[l] =co [l] + 1
            
# C End

# D Begin

for m in np.arange(n_bins+1):
    co[m] = co[m] / dr[m] * 1000 
    
# D End

# E Begin
co_log = []

for n in np.arange(n_bins + 1):
    co_log.append(co[n] * np.log(10) * rc[n])
# E End    
 

##############################################################################
############################################################## visualization #
##############################################################################

print('\n+++ plotting has begun...')

fig, ax = plt.subplots(2)
fig.set_size_inches(8.27,11.69)

#----------------------------------------------------------------plot linearly

ax[0].yaxis.set_major_locator(plt.MultipleLocator(2e12))
ax[0].yaxis.set_minor_locator(plt.MultipleLocator(0.5e12))

ax[0].xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax[0].yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax[0].ticklabel_format(axis='both', style='sci', scilimits=(0,0))

ax[0].set(title = 'Lineare Darstellung des Tropfenspektrums')

ax[0].step(rc, co,
           ls        = '-',
           color     = "blue",
           linewidth = 1) # Here the histrogramm-plot is generated

ax[0].set(xlabel = r'Tropfenradius $r$ in m')
ax[0].set(ylabel = r'$\mathrm{d}N/\mathrm{d}r$ $(\mathrm{ \frac{1}{m} }$)')

ax[0].set(xlim = (r_min,  r_max))
ax[0].set(ylim = (0e12, 1e13))



#---------------------------------------------------------plot logarithmically

#ax[1].xaxis.set_major_locator(plt.MultipleLocator(200))
#ax[1].xaxis.set_minor_locator(plt.MultipleLocator(50))

ax[1].yaxis.set_major_locator(plt.MultipleLocator(0.2e8))
ax[1].yaxis.set_minor_locator(plt.MultipleLocator(0.05e8))
ax[1].yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax[1].set(title = 'Logaritmische Darstellung des Tropfenspektrums')

ax[1].set(xscale = 'log')

ax[1].step(rc, co_log,
           ls        = '-',
           color     = "blue",
           linewidth = 1) # Here the histogramm plot is generated

ax[1].set(xlabel = r'Tropfenradius $r$ in m')
ax[1].set(ylabel = r'$\mathrm{d}N/\mathrm{d}\,\log_{10}(r)$ $(\mathrm{ ??? })$')

ax[1].set(xlim = (r_min, r_max))
ax[1].set(ylim = (0.0e8, 1.2e8))



#--------------------------------------------------------------------save plot

fig.tight_layout(pad=3.0)

plt.savefig("wp-03-Steding-Alexander-plot.pdf", dpi=300)

print('+++ plotting has ended...')
