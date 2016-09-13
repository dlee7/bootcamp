import numpy as np
import scipy.stats
import bootcamp_utils
import matplotlib.pyplot as plt
import seaborn as sns

rc = ('lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18)
sns.set(rc=rc)

data_txt = np.loadtxt('data/collins_switch.csv', delimiter = ',')

iptg = data.txt[:,0]
gfp = data.txt[:,1]

plt.plot(iptg, gfp)
plt.xlabel('IPTG (mM)')
plt.ylabel('Normalized GFP')
plt.show()
