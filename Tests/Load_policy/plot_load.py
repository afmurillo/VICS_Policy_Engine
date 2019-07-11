
import numpy as np
import matplotlib.pyplot as plt
#from pylab import figure, plot, xlabel, grid, hold, legend, title, savefig
from pylab import savefig
#from matplotlib.font_manager import FontProperties
import sys

one_policy    =   np.array([1.730, 1.590, 1.596, 1.594, 1.587, 1.592, 1.584, 1.605, 1.703, 1.710])
ten_policy   =    np.array([1.598, 1.590, 1.606, 1.617, 1.607, 1.587, 1.574, 1.714, 1.586, 1.602])
tenn_policy  =    np.array([1.651, 1.606, 1.586, 1.593, 1.585, 1.596, 1.594, 1.594, 1.719, 1.599])
tennn_policy =    np.array([1.593, 1.641, 1.726, 1.815, 1.600, 1.606, 1.688, 1.588, 1.588, 1.610])
tennnn_policy =   np.array([1.714, 1.785, 1.641, 1.630, 1.686, 1.647, 1.658, 1.698, 1.736, 1.641])
tennnnn_policy =  np.array([2.431, 2.346, 2.409, 2.277, 2.376, 2.293, 2.292, 2.296, 2.307, 2.418])
tennnnnn_policy = np.array([9.566, 9.643, 9.524, 9.464, 9.621, 10.071, 9.482, 9.514, 9.746, 9.677, 9.545, 9.511, 9.612])

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

#xlabel('t')
#grid(True)
#hold(True)
#lw = 1

#plot(t, x1, 'b', linewidth=lw)
#plot(t, xy, 'r', linewidth=lw)
#plot(t, x2, 'g', linewidth=lw)

#legend((r'$L101$', r'$L102$', r'$L103$'), prop=FontProperties(size=16))
#title('Tank Levels with Control')
x=np.array([1, 10, 100, 1000, 1000, 100000, 1000000])

lw=1

plt.figure()
plt.errorbar(x, mean_values, yerr=std_values, linewidth=lw)
plt.xlabel('Number of Rules in Policy File')
plt.ylabel('Time(s)')
plt.grid(True)
plt.title('Policy Parsing Time')

savefig(sys.argv[1]+".png", dpi=100)


