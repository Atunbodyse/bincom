from collections import  Counter

# sample data of colors worn throughout the week

colors_worn = ['red', 'blue', 'green', 'red', 'yellow', 'blue', 'red']

# calculate the mean color

color_counts = Counter(colors_worn)
total_colors = len(colors_worn)
mean_color = max(color_counts, key=lambda x: color_counts[x]/total_colors)

print("the mean color is:",mean_color)
