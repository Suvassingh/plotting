
import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.linspace(-10, 10, 100)
m = 2  # Slope
c = -1  # Intercept
y = m * x + c

# Geometrical plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=f"y = {m}x + {c}", color='blue')
plt.axhline(0, color='black', linewidth=0.8, linestyle="--")  # x-axis
plt.axvline(0, color='black', linewidth=0.8, linestyle="--")  # y-axis
plt.scatter([0], [c], color="red", label=f"Intercept (0, {c})")
plt.title("Geometric Interpretation of y = mx + c")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.grid()
plt.show()



distance = np.linspace(0, 100, 100)
m_cost_per_mile = 2  # $ per mile
c_base_fee = 50  # Base fee in $
cost = m_cost_per_mile * distance + c_base_fee

# Plot
plt.figure(figsize=(8, 6))
plt.plot(distance, cost, label="Cost = 2 × Distance + 50", color='green')
plt.title("Car Rental Cost")
plt.xlabel("Distance (miles)")
plt.ylabel("Cost ($)")
plt.axhline(0, color='black', linewidth=0.8, linestyle="--")  # x-axis
plt.axvline(0, color='black', linewidth=0.8, linestyle="--")  # y-axis
plt.grid()
plt.legend()
plt.grid(visible=True, which='both')
plt.show()