import numpy as np

# 2 smaller objects orbit a larger, heavier object in the middle
m = np.array([1, 10, 1])
x = np.array([-1, 0.0, 1])
y = np.array([0, 0.0, 0])
vx = np.array([0, 0, 0])
vy = np.array([-3.5, 0, 3.5])


#the values are based on https://arxiv.org/pdf/math/0011268.pdf
#m = np.array([1, 1, 1])
#x = np.array([-0.97000436, 0.0, 0.97000436])
#y = np.array([0.24208753, 0.0, -0.24208753])
#vx = np.array([0.4662036850, -0.933240737, 0.4662036850])
#vy = np.array([0.4323657300, -0.86473146, 0.4323657300])
