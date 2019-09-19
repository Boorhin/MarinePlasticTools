import os, sys, datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from scipy.signal import butter, filtfilt
import matplotlib.ticker as ticker
import matplotlib.patheffects as pe

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filtfilt(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = filtfilt(b, a, data)
    return y

WorkingDir = '/media/julien/eSATA1/Julien/Marine plastics/Balnakeil Bin/Weight'
File = 'Weight_Data.txt'

DATA  = np.genfromtxt(WorkingDir+os.sep+File, dtype=[('Date','datetime64[D]'),('Weight', 'float32'), ('Deviation', 'float32')], delimiter ='\t', skip_header = 1)

Duration = np.diff(DATA['Date']).astype('timedelta64[h]')
Days = DATA['Date'][:-1] + Duration/2
Days = [x.tolist() for x in Days]
Rate = DATA['Weight'][1:]/Duration.astype(float)*24

cutoff = 1
fs = 4
Smooth = butter_lowpass_filtfilt(Rate, cutoff, fs)

fig2 = plt.figure()
ax = fig2.add_subplot(111)
fig2.suptitle('Rate and cumulative weight of marine plastics recovered at Balnakeil Beach', fontsize=32)
ax.xaxis_date()

ax.xaxis.set_ticks_position('bottom')
ax.xaxis.set_tick_params(which='major', direction = 'out', width=2, length = 20)
ax.xaxis.set_tick_params(which='minor', direction = 'out', width=2, length = 0)
ax.xaxis.set_minor_formatter(mdates.DateFormatter('%b %y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator(bymonthday=15))
#ax.xaxis.set_major_locator(mdates.MonthLocator(bymonthday=1, interval=1))
ax.set_xlim(DATA['Date'][0].tolist(), DATA['Date'][-1].tolist())
ax.set_xlabel('Date', fontsize = 16)
ax.set_ylabel('Cumulative weight (kg)', fontsize = 16)
ax.tick_params(axis='y', colors='midnightblue')
ax.yaxis.label.set_color('midnightblue')
ax.xaxis.set_major_formatter(ticker.NullFormatter())
ax2 = ax.twinx()
ax.bar(Days, DATA['Weight'].cumsum()[1:], width=Duration.astype(float)/24, yerr = DATA['Deviation'].cumsum()[1:], align="center", color= 'midnightblue', edgecolor ='aliceblue')
ax2.plot(Days, Rate, lw= 2, c ='steelblue', path_effects=[pe.Stroke(linewidth=5, foreground='w'), pe.Normal()])
#ax2.plot(Days, Smooth, lw= 3, ls='--', c='r')
ax2.xaxis.set_major_formatter(ticker.NullFormatter())
ax2.xaxis.set_major_locator(mdates.MonthLocator(bymonthday=1, interval=1))

ax2.set_ylabel('Rate (kg/day)', fontsize = 16)
ax2.yaxis.label.set_color('steelblue')
ax2.spines['right'].set_color('steelblue')
ax2.tick_params(axis='y', colors='steelblue')
#ax2.set_yscale('log')
ax2.set_ylim(0.1,60)
ax2.yaxis.set_major_formatter(ticker.FormatStrFormatter('%3.f'))
ax2.annotate(
    'Frequent beach cleans',
    xy=(Days[4], Rate[4]), arrowprops=dict(arrowstyle='fancy', connectionstyle="arc3,rad=-0.2",ec="w",fc='k'), xytext=(Days[7], Rate[4]+5), fontsize=12, backgroundcolor ='w')
ax2.annotate(
    'Storm Aileen',
    xy=(Days[14], Rate[14]), arrowprops=dict(arrowstyle='fancy', connectionstyle="arc3,rad=-0.2",ec="w",fc='k'), xytext=(Days[16], Rate[14]+10), fontsize=12, backgroundcolor ='w')

ax2.annotate(
     'Storm Caroline1',
    xy=(Days[23], Rate[23]), arrowprops=dict(arrowstyle='fancy', connectionstyle="arc3,rad=-0.2",ec="w",fc='k'), xytext=(Days[17], Rate[23]-10), fontsize=12)
ax2.annotate(
    'Caroline2 (140 kg/day)',
    xy=(Days[25], Rate[25]-80), arrowprops=dict(arrowstyle='fancy', connectionstyle="arc3,rad=-0.2",ec="w",fc='k'), xytext=(Days[26], Rate[25]-85), fontsize=12)
ax2.annotate(
    'Storms Dylan + Eleanor',
    xy=(Days[28], Rate[28]), arrowprops=dict(arrowstyle='fancy', connectionstyle="arc3,rad=-0.2",ec="w",fc='k'), xytext=(Days[30], Rate[28]+10), fontsize=12, backgroundcolor ='w')
ax2.annotate(
    'Unamed Storm',
    xy=(Days[36], Rate[36]), arrowprops=dict(arrowstyle='fancy', connectionstyle="arc3,rad=-0.2",ec="w",fc='k'), xytext=(Days[37], Rate[36]+10), fontsize=12, backgroundcolor ='w')
ax2.annotate(
    'Frequent beach cleans',
    xy=(Days[51], Rate[51]), arrowprops=dict(arrowstyle='fancy', connectionstyle="arc3,rad=-0.2",ec="w",fc='k'), xytext=(Days[52], Rate[51]+10), fontsize=12, backgroundcolor ='w')
ax2.annotate(
    'Unamed Storm',
    xy=(Days[59], Rate[59]), arrowprops=dict(arrowstyle='fancy', connectionstyle="arc3,rad=-0.2",ec="w",fc='k'), xytext=(Days[55], Rate[55]+10), fontsize=12, backgroundcolor ='w')
ax2.annotate(
    'Many storms (Gareth)\n& ranger starting',
    xy=(Days[64], Rate[64]), arrowprops=dict(arrowstyle='fancy', connectionstyle="arc3,rad=-0.2",ec="w",fc='k'), xytext=(Days[59], Rate[64]+5), fontsize=12, backgroundcolor ='w')
ax2.annotate(
    'northern storms \n Cape wrath beach clean',
    xy=(Days[71], Rate[71]), arrowprops=dict(arrowstyle='fancy', connectionstyle="arc3,rad=-0.2",ec="w",fc='k'), xytext=(Days[61], Rate[71]+10), fontsize=12, backgroundcolor ='w')
ax2.annotate(
    'Kik Plastic\nbeach clean',
    xy=(Days[81], Rate[81]), arrowprops=dict(arrowstyle='fancy', connectionstyle="arc3,rad=-0.2",ec="w",fc='k'), xytext=(Days[74], Rate[81]+5), fontsize=12, backgroundcolor ='w')

plt.show()
