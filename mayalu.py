import numpy as np
import matplotlib.pyplot as plt

# Constants
k = 10  # Spring constant (N/m)
m = 0.5  # Mass (kg)
omega = np.sqrt(k / m)  # Angular frequency (rad/s)

# Time array
t = np.linspace(0, 10, 1000)  # Time from 0 to 10 seconds

# Displacement equation
x = np.sin(omega * t)

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(t, x, label='Displacement (m)')
plt.title('Vertical Oscillation of a Spring')
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.grid(True)
plt.legend()
plt.show()
