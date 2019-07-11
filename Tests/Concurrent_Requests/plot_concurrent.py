import numpy as np
import matplotlib.pyplot as plt
#from pylab import figure, plot, xlabel, grid, hold, legend, title, savefig
from pylab import savefig
#from matplotlib.font_manager import FontProperties
import sys

one_rule_t_r = [28.204, 28.756, 28.552, 28.964, 28.820, 28.588, 29.028, 28.944, 28.852, 28.756]
one_rule_f_r = [58.508, 58.708, 58.580, 59.132, 59.676, 58.284, 58.752, 58.832, 59.148, 59.164]
one_rule_h_r = [60+59.216, 60+57.404, 60+57.256, 60+58.004, 60+56.812, 60+57.340, 60+57.940, 60+56.640, 60+56.940, 60+55.980]

a=np.mean(one_rule_t_r)
b=np.mean(one_rule_f_r)
c=np.mean(one_rule_h_r)

one_mean_values=np.array([a, b, c])

a=np.std(one_rule_t_r)
b=np.std(one_rule_f_r)
c=np.std(one_rule_h_r)

one_std_values = np.array([a,b,c])


ten_rules_t_r = [29.152, 29.064, 29.288, 29.104, 29.452, 28.892, 29.000, 29.172, 28.788, 28.872]
ten_rules_f_r = [58.336, 57.952, 58.280, 57.976, 58.052, 58.460, 58.708, 58.640, 58.780, 58.628]
ten_rules_h_r = [60+57.656, 60+57.456, 60+58.204, 60+56.948, 60+58.440, 60+58.332, 60+59.848, 120+57.668, 120+58.952, 60+57.044]


a=np.mean(ten_rules_t_r)
b=np.mean(ten_rules_f_r)
c=np.mean(ten_rules_h_r)

ten_mean_values=np.array([a, b, c])

a=np.std(ten_rules_t_r)
b=np.std(ten_rules_f_r)
c=np.std(ten_rules_h_r)

ten_std_values = np.array([a,b,c])

hundred_rules_t_r = [28.536, 29.052, 29.032, 28.876, 28.700, 29.232, 28.816, 28.788, 28.904, 28.832]
hundred_rules_f_r = [58.176, 58.820, 58.300, 58.384, 58.036, 58.588, 58.784, 58.532, 58.308, 58.472]
hundred_rules_h_r = [60+58.392, 60+57.208, 60+57.472, 60+56.804, 60+58.372, 60+56.828, 60+57.580, 60+57.080, 60+56.348, 60+57.692]


a=np.mean(hundred_rules_t_r)
b=np.mean(hundred_rules_f_r)
c=np.mean(hundred_rules_h_r)

hundred_mean_values=np.array([a, b, c])

a=np.std(hundred_rules_t_r)
b=np.std(hundred_rules_f_r)
c=np.std(hundred_rules_h_r)

hundred_std_values = np.array([a,b,c])
 
thousand_rules_t_r = [28.472, 29.060, 29.220, 29.184, 29.012, 28.908, 28.956, 28.728, 29.016, 28.820]
thousand_rules_f_r = [58.196, 58.332, 58.624, 58.540, 57.664, 58.024, 57.932, 58.476, 58.620, 58.088]
thousand_rules_h_r = [60+57.420, 60+57.232, 60+57.188, 60+58.580, 60+57.716, 60+56.960, 60+56.856, 60+57.376, 60+56.416, 60+56.832]

a=np.mean(thousand_rules_t_r)
b=np.mean(thousand_rules_f_r)
c=np.mean(thousand_rules_h_r)

thousand_mean_values=np.array([a, b, c])

a=np.std(thousand_rules_t_r)
b=np.std(thousand_rules_f_r)
c=np.std(thousand_rules_h_r)

thousand_std_values = np.array([a,b,c])


ten_thousand_rules_t_r = [29.000, 28.996, 29.100, 28.884, 29.164, 28.644, 28.796, 28.860, 29.036, 29.560]
ten_thousand_rules_f_r = [58.460, 58.396, 58.400, 58.888, 58.772, 57.900, 57.968, 58.132, 58.064, 58.192]
ten_thousand_rules_h_r = [60+56.056, 60+56.652, 60+56.464, 60+57.336, 60+56.712, 60+56.768, 60+57.240, 60+57.780, 60+57.088, 60+57.388]

a=np.mean(ten_thousand_rules_t_r)
b=np.mean(ten_thousand_rules_f_r)
c=np.mean(ten_thousand_rules_h_r)

ten_thousand_mean_values=np.array([a, b, c])

a=np.std(ten_thousand_rules_t_r)
b=np.std(ten_thousand_rules_f_r)
c=np.std(ten_thousand_rules_h_r)

ten_thousand_std_values = np.array([a,b,c])


hundred_thousand_rules_t_r = [28.876, 28.872, 29.144, 28.744, 28.856, 29.176, 29.100, 29.488, 29.164, 29.288]
hundred_thousand_rules_f_r = [58.076, 58.584, 58.220, 58.300, 58.164, 57.840, 58.340, 58.732, 58.356, 58.304]
hundred_thousand_rules_h_r = [60+56.948, 60+56.560, 60+56.844, 60+56.696, 60+57.796, 60+57.152, 60+57.016, 60+56.384, 60+56.772, 60+56.400]

a=np.mean(hundred_thousand_rules_t_r)
b=np.mean(hundred_thousand_rules_f_r)
c=np.mean(hundred_thousand_rules_h_r)

hundred_thousand_mean_values=np.array([a, b, c])

a=np.std(hundred_thousand_rules_t_r)
b=np.std(hundred_thousand_rules_f_r)
c=np.std(hundred_thousand_rules_h_r)

hundred_thousand_std_values = np.array([a,b,c])

x=np.array([25, 50, 100])

lw=1

plt.figure()
plt.errorbar(x, one_mean_values, yerr=one_std_values, linewidth=lw)
plt.errorbar(x, ten_mean_values, yerr=ten_std_values, linewidth=lw)
plt.errorbar(x, hundred_mean_values, yerr=hundred_std_values, linewidth=lw)
plt.errorbar(x, thousand_mean_values, yerr=thousand_std_values, linewidth=lw)
plt.errorbar(x, ten_thousand_mean_values, yerr=ten_thousand_std_values, linewidth=lw)
plt.errorbar(x, hundred_thousand_mean_values, yerr=hundred_thousand_std_values, linewidth=lw)

plt.xlabel('Number of Concurrent Requests')
plt.ylabel('Time(s)')
plt.legend((r'$1 Rule$', r'$10 Rules$', r'$100 Rules$', r'$1000 Rules$', r'$10000 Rules$', r'$100000 Rules$'), loc='upper left')
plt.grid(True)
plt.title('Request Response Time')

savefig(sys.argv[1]+".png", dpi=100)


