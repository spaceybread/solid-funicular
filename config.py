import numpy as np

#template
#m = np.array([mass of object 1, mass of object 2, mass of object 3])
#x = np.array([initial x of object 1, initial x of object 2, initial x of object 3])
#y = np.array([initial y of object 1, initial y of object 2, initial y of object 3])
#vx = np.array([initial dx of object 1, initial dx of object 2, initial dx of object 3])
#vy = np.array([initial dy of object 1, initial dy of object 2, initial dy of object 3])

#m: mass
#x, y: initial x, y coordinates
#dx, dy: intial velocities in directions x and y


# 2 smaller objects orbit a larger, heavier object in the middle
m = np.array([1, 10, 1])
x = np.array([-1, 0.0, 1])
y = np.array([0, 0.0, 0])
vx = np.array([0, 0, 0])
vy = np.array([-3.5, 0, 3.5])


#the values are based on https://arxiv.org/pdf/math/0011268.pdf for the stable 3 body 8 shape
#m = np.array([1, 1, 1])
#x = np.array([-0.97000436, 0.0, 0.97000436])
#y = np.array([0.24208753, 0.0, -0.24208753])
#vx = np.array([0.4662036850, -0.933240737, 0.4662036850])
#vy = np.array([0.4323657300, -0.86473146, 0.4323657300])
