from collections import Counter

# Sample data of colors worn throughout the week
colors_worn = ['red', 'blue', 'green', 'red', 'yellow', 'blue', 'red']

# Calculate the color mostly worn
color_counts = Counter(colors_worn)
most_common_color = color_counts.most_common(1)[0][0]

print("The color mostly worn is:", most_common_color)