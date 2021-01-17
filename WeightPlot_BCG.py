import os, sys, datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from scipy.signal import butter, filtfilt


def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filtfilt(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = filtfilt(b, a, data)
    return y


# Data directory: MarinePlasicTools/Weight
# WorkingDir = os.getcwd()
WorkingDir = 'Weight'
File = 'BeachCleanGirl_Weight.txt'

DATA  = np.genfromtxt(WorkingDir+os.sep+File, dtype=[('Date','datetime64[D]'),('Weight', 'float32')], delimiter ='\t', skip_header = 1)

Duration = np.diff(DATA['Date']).astype('timedelta64[h]')
Days = DATA['Date'][:-1] + Duration/2
Days = [x.tolist() for x in Days]
Rate = DATA['Weight'][1:]/Duration.astype(float)*24
# Filter
cutoff = 1                   
fs = 20
Smooth = butter_lowpass_filtfilt(Rate, cutoff, fs)

fig2 = plt.figure()
ax = fig2.add_subplot(111)
fig2.suptitle('Rate and cumulative weight of marine plastics recovered at Lee-on-the-Solent', fontsize=16)
ax.xaxis_date()
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=7))
ax2 = ax.twinx()
ax.bar(Days, DATA['Weight'].cumsum()[1:], width=Duration.astype(float)/24, align="center", color= 'grey')
ax2.plot(Days, Rate, lw= 2, c ='r')
ax2.plot(Days, Smooth, lw= 3, ls='--', c ='r')
ax.set_ylabel('Cumulative weight (kg)')
ax2.set_ylabel('Rate (kg/day)')
ax2.yaxis.label.set_color('red')
ax2.spines['right'].set_color('red')
ax2.tick_params(axis='y', colors='red')
ax.set_xlabel('Date')
fig2.autofmt_xdate()
plt.show()


    

