import numpy as np
import matplotlib.pyplot as plt

Time = np.arange(34, dtype=np.float)
Years = Time + 2016
StockBal  = 1000.
StockOSM  = 5000.
StockPol  = 500.
StockDro  = 200.
RateBal = 4*365.25
RateOSM = 3*365.25
RatePol = 2*365.25
RateDro = 1*365.25
BCBal = 1000.
BCOSM = 600.
BCPol = 200.
BCDro = 200.
MassBal, MassOSM, MassPol,MassDro      =np.zeros(len(Time)), np.zeros(len(Time)), np.zeros(len(Time)), np.zeros(len(Time))
CleanBal, CleanOSM, CleanPol, CleanDro = np.zeros((3,len(Time))), np.zeros((3,len(Time))), np.zeros((3,len(Time))), np.zeros((3,len(Time)))

MassBal = Time*RateBal 
MassOSM = Time*RateOSM 
MassPol = Time*RatePol 
MassDro = Time*RateDro

for mass in [MassBal, MassOSM, MassPol,MassDro]:
    mass[2:] *=2  #Doubling of rates in 2019
    mass[5:] *=1.5 #TotalAramco factory

MassBal += StockBal
MassOSM += StockOSM
MassPol += StockPol
MassDro += StockDro

CleanBal[1] += BCBal
CleanOSM[1] += BCOSM
CleanPol[1] += BCPol
CleanDro[1] += BCDro

CleanBal[2] += BCBal+3000
CleanOSM[2] += BCOSM+2500
CleanPol[2] += BCPol+1500
CleanDro[2] += BCDro+500

plt.xkcd()
Width = 0.5
Fig, ax = plt.subplots(1,3)
Fig.suptitle('Major plastic accumulations in Plastic@Bay area')
for i, ax in enumerate(Fig.axes):
    ax.bar(Years, MassBal-CleanBal[i,:].cumsum(), Width, label='Balnakeil' )
    ax.bar(Years, MassOSM-CleanOSM[i,:].cumsum(), Width, bottom=MassBal-CleanBal[i,:].cumsum(), label='Oldshoremore' )
    ax.bar(Years, MassPol-CleanPol[i,:].cumsum(), Width, bottom=MassBal-CleanBal[i,:].cumsum() + MassOSM-CleanOSM[i,:].cumsum(), label ='Polin' )
    ax.bar(Years, MassDro-CleanDro[i,:].cumsum(), Width, bottom=MassBal-CleanBal[i,:].cumsum() + MassOSM-CleanOSM[i,:].cumsum() + MassPol-CleanPol[i,:].cumsum(), label ='Droman')
    ax.set_xlabel('Years')
    ax.set_ylabel('Volume in kg')
    ax.set_ylim(0,250000)
    ##plt.annotate(
    ##    'Doubling of production\n with Shell and Exxon\nsuperfactories',
    ##    xy=(Years[3], ScenarNYT_ShellExxon[3]), arrowprops=dict(arrowstyle='->'), xytext=(2014, 2.5e13), fontsize=10)
    ##plt.annotate(
    ##    'Total and Saudi\nAramco superfactory',
    ##    xy=(Years[5], ScenarNYT_ShellExxon_TotSaudi[5]), arrowprops=dict(arrowstyle='->'), xytext=(2023, 3.5e13), fontsize=10)
    ax.legend()
Fig.axes[0].set_title('Projections with no Beachclean\nEstimates from Plastic@Bay surveys\nBaln +1.5 t/y, OSM +1 t/y, Polin +0.7 t/y, Drom +0.2 t/y')
Fig.axes[1].set_title('Projections with current\nCommunity-led beachcleans (seasonal)\nBaln -1t/y, OSM -0.6 t/y, Polin -0.2 t/y, Drom -0.2 t/y')
Fig.axes[2].set_title('Projections with Community-led beachcleans\n+ Plastic@bay ranger\nBaln -4t/y, OSM -3.1 t/y, Polin -1.7 t/y, Drom -0.7 t/y')
#Fig.tight_layout()
plt.show()
