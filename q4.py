import numpy as np

# Assign numerical values to colors
colors = {'red': 1, 'blue': 2, 'green': 3, 'yellow': 4, 'purple': 5}

# List of colors worn throughout the week
week_colors = ['red', 'blue', 'green', 'red', 'yellow', 'green', 'purple']

# Assign numerical values based on the color dictionary
numeric_values = [colors[color] for color in week_colors]

# Calculate the variance
variance = np.var(numeric_values)

print("Variance of colors worn throughout the week:", variance)
