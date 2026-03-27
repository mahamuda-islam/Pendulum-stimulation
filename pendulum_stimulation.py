import numpy as np
import matplotlib.pyplot as plt

# Parameters
g = 9.8
L = 1.0
theta0 = 0.5

t = np.linspace(0, 10, 500)

omega = np.sqrt(g / L)
theta = theta0 * np.cos(omega * t)

# Convert to x, y positions
x = L * np.sin(theta)
y = -L * np.cos(theta)

# Plot pendulum motion frame by frame
for i in range(len(t)):
    plt.clf()
    
    # Draw rod
    plt.plot([0, x[i]], [0, y[i]], 'k-')
    
    # Draw bob
    plt.plot(x[i], y[i], 'ro')
    
    plt.xlim(-1.2, 1.2)
    plt.ylim(-1.2, 0.2)
    plt.title("Pendulum Motion Animation")
    
    plt.pause(0.02)

plt.show()