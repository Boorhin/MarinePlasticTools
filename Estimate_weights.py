import os, sys, csv, datetime, glob
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as mdates

WorkingDir = '/media/julien/eSATA1/Julien/Marine plastics/Balnakeil Bin/Data'
FileList = sorted(glob.glob(WorkingDir+os.sep+'*.txt'))

#d= {}
### data, nb vs weight
W = [17., 17., 20.]
N = [467., 421., 517.]
R = np.ones(len(W))
for i in range(len(W)):
     R[i]= W[i]/N[i]
mR,dR = np.mean(R), np.std(R)

for i in range(len(FileList)):
    with open(FileList[i]) as f:
        lines = f.readlines()[4:]
    print FileList[i][62:]
    Tot = 0
    for j in range(len(lines)):
        line = lines[j].strip('\n')
        if line: #check empty
            line = line.split('\t')
            label, value = line[0], line[-1]
            if value:
                Tot += int(value)
    print Tot,'\t', mR*Tot, '\t', dR*Tot, '\n'
##                if label in d:
##                    d[label] += int(value)
##                else:
##                    d[label] = int(value)
