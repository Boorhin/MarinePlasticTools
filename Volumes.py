import numpy as np
import matplotlib.pyplot as plt

Time = np.arange(36, dtype=np.float)
Years = Time + 2015
Stock                          = 6.9*10**12 # kg in 2015
RateNYT                        = 5*10**11 #kg/y
RateNG                         = 3*10**11 #kg/y
RateNYT_ShellExxon             = Time*RateNYT
RateNYT_ShellExxon[3:]        *= 2
ScenarNYT_ShellExxon_TotSaudi =np.zeros(len(Time))
ScenarNYT_ShellExxon_TotSaudi[:5]  = RateNYT_ShellExxon[:5]
ScenarNYT_ShellExxon_TotSaudi[5:]  = RateNYT_ShellExxon[5:]  * 1.5

StockEvol = np.zeros(len(Years))
StockEvol += Stock
ScenarNYT                         = StockEvol + Time*RateNYT
ScenarNG                          = StockEvol + Time*RateNG
ScenarNYT_ShellExxon              = StockEvol + RateNYT_ShellExxon
ScenarNYT_ShellExxon_TotSaudi     = StockEvol + ScenarNYT_ShellExxon_TotSaudi


plt.xkcd()
Fig, ax = plt.subplots(1,1)#title='World Plastic production simulation')
plt.title('World Plastic production simulation\nOf which \n80% will go in the environment\n 40% will be used once')
ax.plot(Years, ScenarNYT, label='NYT rates' )
ax.plot(Years, ScenarNG , label='NatGeo rates' )
ax.plot(Years, ScenarNYT_ShellExxon, label ='NYT rates + ExxonShell' )
ax.plot(Years, ScenarNYT_ShellExxon_TotSaudi, label ='NYT rates + ExxonShell\n         + TotalAramco')
ax.set_xlabel('Years')
ax.set_ylabel('Volume in kg')
plt.annotate(
    'Doubling of production\n with Shell and Exxon\nsuperfactories',
    xy=(Years[3], ScenarNYT_ShellExxon[3]), arrowprops=dict(arrowstyle='->'), xytext=(2014, 2.5e13), fontsize=10)
plt.annotate(
    'Total and Saudi\nAramco superfactory',
    xy=(Years[5], ScenarNYT_ShellExxon_TotSaudi[5]), arrowprops=dict(arrowstyle='->'), xytext=(2023, 3.5e13), fontsize=10)
ax.legend()
Fig.tight_layout()
plt.show()
