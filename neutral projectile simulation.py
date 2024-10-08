import numpy as np
import matplotlib.pyplot as plt

g = 9.81  #avg graviational pull of earth
v0 = 800  #velocity of a hgih speed projectile m/s 
angle = 30 #degrees
C_d = 0.295  #drag coefficient of a bullet
rho = 1.225  #air density kg/m^3 
A = 0.000145  #cross section at m^2
mass = 0.0097  #bullet mass in kg

dt = 0.01  
t_total = 10  
times = np.arange(0, t_total, dt)

#int
x = 0
y = 0
vx = v0 * np.cos(np.radians(angle))
vy = v0 * np.sin(np.radians(angle))

x_positions = []
y_positions = []

for t in times:
 #drag force
    v = np.sqrt(vx**2 + vy**2)
    F_d = 0.5 * C_d * rho * A * v**2

    #acceleration
    ax = -F_d * vx / v / mass
    ay = -g - F_d * vy / v / mass

    #velocity
    vx += ax * dt
    vy += ay * dt

    #position
    x += vx * dt
    y += vy * dt

    x_positions.append(x)
    y_positions.append(y)

    if y < 0: #bullet falls to the floor
        break

plt.figure()
plt.plot(x_positions, y_positions)
plt.title('Neutral Projectile Motion Simulation')
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.ylim(0, max(y_positions) + 10)
plt.grid(True)
plt.show()
