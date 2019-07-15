import numpy as np
import matplotlib.pyplot as plt
#from pylab import figure, plot, xlabel, grid, hold, legend, title, savefig
from pylab import savefig
#from matplotlib.font_manager import FontProperties
import sys

no_policy =       [1.248, 1.389, 1.108, 1.141, 1.248, 1.210, 1.115, 1.236, 1.213, 1.116]
one_policy =      [0.836, 1.206, 1.225, 1.169, 1.259, 1.113, 1.220, 1.138, 1.236, 1.101]
ten_policy =      [1.149, 1.122, 1.153, 1.235, 1.128, 1.143, 1.217, 1.231, 1.126, 1.109]
tenn_policy =     [1.117, 1.117, 1.236, 1.249, 1.129, 1.136, 1.272, 1.131, 1.220, 1.148]
tennn_policy =    [1.132, 1.107, 1.372, 1.227, 1.107, 1.212, 1.152, 1.120, 1.098, 1.122]
tennnn_policy =   [1.154, 1.285, 1.098, 1.247, 1.115, 1.336, 1.116, 1.132, 1.131, 1.262]
tennnnn_policy =  [1.215, 1.126, 1.115, 1.163, 1.236, 1.143, 1.306, 1.179, 1.222, 1.150]
tennnnnn_policy = [1.509, 1.487, 1.313, 1.293, 1.448, 1.492, 1.296, 1.420, 1.413, 1.423]

z=np.mean(no_policy)
a=np.mean(one_policy)
b=np.mean(ten_policy)
c=np.mean(tenn_policy)
d=np.mean(tennn_policy)
e=np.mean(tennnn_policy)
f=np.mean(tennnnn_policy)
g=np.mean(tennnnnn_policy)

mean_values=np.array([a, b, c, d, e, f, g])

print mean_values

a=np.std(one_policy)
b=np.std(ten_policy)
c=np.std(tenn_policy)
d=np.std(tennn_policy)
e=np.std(tennnn_policy)
f=np.std(tennnnn_policy)
g=np.std(tennnnnn_policy)


std_values=np.array([a, b, c, d, e, f, g])


print std_values
x=np.array([1, 10, 100, 1000, 1000, 100000, 1000000])

lw=1

plt.figure()
plt.errorbar(x, mean_values, yerr=std_values, linewidth=lw)
plt.xlabel('Number of Rules in Policy File')
plt.ylabel('Time(s)')
plt.grid(True)
plt.title('Request Response Time')
plt.ylim((0, 2))  
savefig(sys.argv[1]+".png", dpi=100)


