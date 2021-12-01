# Imports
import matplotlib.pyplot as plt
import numpy as np
import math

# User Editable Variables -----
lower_bounds = 0 # Lower X bounds
upper_bounds = 1 # Upper X bounds
precision = 1000000 # Number of splits between lower and upper bounds (more makes the answer more accurate)
graph_y_upper_lim = 20 # Graphing view scope of y axis (upper limit)
graph_y_lower_lim = 0 # Graphing view scope of y axis (lower limit)
graph_thickness = 200 # Don't change this unless you know what you're doing

def f(x):
    return x * (math.e ** (x ** 3)) # Function to be evaluated

# User Editable Variables -----

# Calculations to find definite integral value
difference = abs(upper_bounds - lower_bounds)
num_of_x_splits = difference * precision

splits = np.linspace(start=lower_bounds, stop=upper_bounds, num=num_of_x_splits)

values_of_split_x = 0

for num in splits:
    values_of_split_x += f(num)

definite_integral = values_of_split_x / precision
definite_integral_approx = round(definite_integral, 2)

# Printing Answers
print("-----")
print("Value of definite integral:", definite_integral)
print("Approximated version:", definite_integral_approx)
print("-----")

# Graphing 
graph_x_lower_lim = lower_bounds - (difference * 0.5)
graph_x_upper_lim = upper_bounds + (difference * 0.5)
plt.xlim([graph_x_lower_lim, graph_x_upper_lim])
plt.ylim([graph_y_lower_lim, graph_y_upper_lim])
plt.title(f"Definite Integral of Function (Shaded Region): {definite_integral_approx} or {definite_integral}", size=15)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
x_1 = np.linspace(start=lower_bounds, stop=upper_bounds, num=difference * graph_thickness)
plt.plot(x_1, f(x_1))
plt.fill_between(x_1, f(x_1), color='blue', alpha=0.2)
plt.show()








