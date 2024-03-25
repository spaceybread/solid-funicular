import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import config

# sep check function
def sp(cor):
    X = np.array(cor[0])
    Y = np.array(cor[1])
    for n in range(len(X)):
        for i in range(len(X)):
            if n != i:
                sep = math.sqrt((X[n] - X[i])**2 + (Y[n] - Y[i])**2)
                if sep < 0.09:
                    return True
    return False
    
# helper function
def r(cor, mass, G):
    X = np.array(cor[0])
    Y = np.array(cor[1])
    vX = np.array(cor[2])
    vY = np.array(cor[3])
    delt = np.array(cor)
    
    for n in range(len(X)):
        dvx, dvy = 0, 0
        
        for i in range(len(X)):
            if n != i:
                sep = math.sqrt((X[n] - X[i])**2 + (Y[n] - Y[i])**2)
                dvx -= (G * mass[i] * (X[n] - X[i])) / sep**3
                dvy -= (G * mass[i] * (Y[n] - Y[i])) / sep**3

        delt[2][n] = dvx
        delt[3][n] = dvy
        
    delt[0] = vX
    delt[1] = vY
    
    return delt

#step function
def step(cor, mass, dt, G):
     if sp(cor) == True: # if the objects collide, the simulation stops
        return cor
     k1 = dt * r(cor, mass, G)
     k2 = dt * r(cor + k1/2, mass, G)
     k3 = dt * r(cor + k2/2, mass, G)
     k4 = dt * r(cor + k3, mass, G)
     
     cor = cor + (k1 + 2*k2 + 2*k3 + k4)/6
     
     return cor

#init
m = config.m
x = config.x
y = config.y
vx = config.vx
vy = config.vy

cords = np.array([x,y,vx,vy])

time = np.linspace(0, 2*6.3259, 2*1001, endpoint=True)
dt = time[1] - time[0]

X = np.zeros((3, len(time)))
Y = np.zeros((3, len(time)))
VX = np.zeros((3, len(time)))
VY = np.zeros((3, len(time)))


#computing values
for _ in range(len(time)):
    cords = step(cords, m, dt, 1)
    X[:, _], Y[:, _], VX[:, _], VY[:, _] = cords[0], cords[1], cords[2], cords[3]
    print(cords)

#plotting
fig, ax = plt.subplots(figsize=(10, 4))

ax.set_xlim(-10.1, 10.1)
ax.set_ylim(-10.1, 10.1)
ax.set_aspect('equal')
ax.grid(True, alpha=0.5)
ax.minorticks_on()
ax.grid(True, alpha=0.3, which='minor')
ax.set_facecolor('black')

line1, = ax.plot([], [], lw=2, alpha=0.2)
line2, = ax.plot([], [], lw=2, alpha=0.2)
line3, = ax.plot([], [], lw=2, alpha=0.2)
scat1 = ax.scatter([], [], marker='o', c='red', s=80)
scat2 = ax.scatter([], [], marker='o', c='blue', s=80)
scat3 = ax.scatter([], [], marker='o', c='green', s=80)

def update(frame):
    i = frame
    
    line1.set_data(X[0, :i], Y[0, :i])
    line2.set_data(X[1, :i], Y[1, :i])
    line3.set_data(X[2, :i], Y[2, :i])
    
    scat1.set_offsets(np.c_[X[0, i], Y[0, i]])
    scat2.set_offsets(np.c_[X[1, i], Y[1, i]])
    scat3.set_offsets(np.c_[X[2, i], Y[2, i]])
    
    return line1, line2, line3, scat1, scat2, scat3

frames = len(time)
ani = FuncAnimation(fig, update, frames=frames, blit=True, interval=5)

plt.show()
