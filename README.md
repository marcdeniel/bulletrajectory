this is a physics simulation of bullet trajectoy
 
bullet's position over time (matplotlib)

gravity at 9.8 m/s

and air drag at 1.225

v0 = initial velocity
angle at launch in relation to the horizontal 
drag force  at   F_d = 0.5 * C_d * rho * A * v**2

and the cross sectional area of the bullet

**Drag Force**
Resistive force in the opposing direction of a projectile's travel through a medium such as air
Drag Force increases proportional to projectile's speed.

we will account for drag force in a horziontal and vertical direction at 
  ax = -F_d * vx / v / mass
  ay = -g - F_d * vy / v / mass

 **velocity**
magnitude = v = sqrt(v_x^2 + v_y^2)
