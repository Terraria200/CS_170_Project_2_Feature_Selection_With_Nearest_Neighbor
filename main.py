import numpy as np

# Load dataset
def load_data(file):
    data = np.loadtxt(file)
    return data[:,0], data[:,1:]
