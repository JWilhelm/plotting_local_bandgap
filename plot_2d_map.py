import numpy as np
import matplotlib.pyplot as plt

# Step 1: Read data from the file
data = []
with open("gap_SCF_EPS_LDOS_0.300_ENERGY_WINDOW_9.000", "r") as file:
    for line in file:
        x, y, f_xy = map(float, line.split())
        data.append((x, y, f_xy))

# Step 2: Extract x, y, and f(x, y) values
x_values = [entry[0] for entry in data]
y_values = [entry[1] for entry in data]
f_xy_values = [entry[2] for entry in data]

# Step 3: Create a grid of x and y values
x_min, x_max = min(x_values), max(x_values)
y_min, y_max = min(y_values), max(y_values)
x_range = np.linspace(x_min, x_max, 100)
y_range = np.linspace(y_min, y_max, 100)
X, Y = np.meshgrid(x_range, y_range)

# Step 4: Interpolate the f(x, y) values on the grid
from scipy.interpolate import griddata

f_xy_grid = griddata((x_values, y_values), f_xy_values, (X, Y), method='cubic')

# Step 5: Create a filled contour plot
plt.figure(figsize=(10, 8))
contour = plt.contourf(X, Y, f_xy_grid, cmap='viridis', levels=100)

# Add color bar
cbar = plt.colorbar(contour)
cbar.set_label('f(x, y)')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Continuous Color Map of f(x, y)')

# Specify the file path where you want to save the plot
output_file = "continuous_color_map.png"

# Save the plot as a PNG file
plt.savefig(output_file)

plt.show()
