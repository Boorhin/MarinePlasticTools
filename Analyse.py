import os, sys, csv, datetime, glob
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as mdates

WorkingDir = '/media/julien/eSATA1/Julien/Marine plastics/Balnakeil Bin/Data'
FileList = sorted(glob.glob(WorkingDir+os.sep+'*.txt'))

d= {}

for i in range(len(FileList)):
    with open(FileList[i]) as f:
        lines = f.readlines()[4:]
    for j in range(len(lines)):
        line = lines[j].strip('\n')
        if line: #check empty
            line = line.split('\t')
            label, value = line[0], line[-1]
            if value:
                if label in d:
                    d[label] += int(value)
                else:
                    d[label] = int(value)
        
KEYS = sorted(d, key=d.get, reverse=True)
VALUES = [d[x] for x in KEYS]
Nb = 20 # nb of max values

fig = plt.figure()
ax = fig.add_subplot(111)
ax.bar(range(Nb), VALUES[:Nb], align='center')
ax.set_xticks(np.arange(Nb))
ax.set_xticklabels(KEYS[:Nb], rotation = 90)
ax.set_xlim([-0.5, Nb-0.5])
plt.tight_layout()
fig.savefig('fig.svg')


### Time frames
# data host
Nb2 = 9
Host  = np.ones(shape=(len(FileList),Nb2))
Rates = np.ones(shape=(len(FileList),Nb2))
Dates = []
Weights = []
for i in range(len(FileList)):
    with open(FileList[i]) as f:
        Lines = f.readlines()[3:]
        if Lines[0].strip('\n'):
            WeightLine = Lines[0].strip('\n')
            W = WeightLine.split('\t')[1]
            Weights.append(W)
        DayOut = dt.datetime.strptime(FileList[i][len(WorkingDir)+1:-10]+'-2017','%m-%d-%Y').date()
        DayIn = dt.datetime.strptime(FileList[i][len(WorkingDir)+7:-4]+'-2017','%m-%d-%Y').date()
        Duration = (DayOut - DayIn)
        Dates.append(DayIn+Duration/2)
        
        
    for j in range(1, len(Lines)):
        line = Lines[j].strip('\n')
        if line: #check empty
            line = line.split('\t')
            L, V = line[0], line[-1]
            if V:
                if L in KEYS[:Nb2]:
                    Host[i][KEYS.index(L)]=V
                    Rates[i][KEYS.index(L)]=V/Duration.days

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.xaxis_date()
ax2.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
ax2.xaxis.set_major_locator(mdates.DayLocator(interval=7))
for k in range(len(Host[0])):
    ax2.plot(Dates, Host[:,k], label=KEYS[k])
ax2.legend()

fig3 = plt.figure()
ax3 = fig3.add_subplot(111)
ax3.xaxis_date()
ax3.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
ax3.xaxis.set_major_locator(mdates.DayLocator(interval=7))
for k in range(len(Host[0])):
    ax2.plot(Dates, Rates[:,k], label=KEYS[k])
ax3.legend()


plt.show()
    

#plt.show()
