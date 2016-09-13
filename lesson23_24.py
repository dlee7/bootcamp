import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import seaborn as sns

xa_high = np.loadtxt('data/xa_high_food.csv', comments = '#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments = '#')

def ecdf(data):
    """compare x, y values for an emprical distribution function"""
    x = np.sort(data)
    y = np.arange(0, 1, 1/len(x))

    return x, y

x_high, y_high = ecdf(xa_high)
plt.plot(x_high, y_high, marker = '.', linestyle = 'none', markersize = 20)
plt.xlabel('Cross-sectional across ()µm)')
plt.ylabel('eCDF')
plt.show()
