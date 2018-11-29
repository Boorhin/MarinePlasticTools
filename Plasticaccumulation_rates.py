import numpy as np
import matplotlib.pyplot as plt
Days = [3,4,5,6,7,8,9,10]
Growth =0.2
Weight= np.ones(20)
fig = plt.figure()
ax = fig.add_subplot(111)
fig.suptitle('20 years simulation of plastic accumulation at Canna Nam Buch')


for j in Days:
    Weight[0]= 365.25*j
    for i in range(1, len(Weight)):
        Weight[i] = Weight[i-1]*(1-Growth)


    ax.plot(Weight[::-1].cumsum(), label = str(j)+'kg/day')

ax.legend(loc=2)
plt.show()
