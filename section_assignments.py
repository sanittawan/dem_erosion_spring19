import numpy as np

np.random.seed(4)
np.random.choice(27, 10, replace=False)
# array([24, 16, 22,  0,  3, 10, 12, 11,  6,  2])
np.random.choice(28, 10, replace=False)
# array([ 4, 16, 11,  5, 25, 12, 27,  7, 22, 18])