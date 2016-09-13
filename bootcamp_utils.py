import numpy as np

def ecdf(data):
    """compare x, y values for an emprical distribution function"""
    x = np.sort(data)
    y = np.arange(0, 1, 1/len(x))

    return x, y
