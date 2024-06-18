import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# Create a plot
plt.plot(x, y, label='Sample Data')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sample Plot')
plt.legend()

# Save the plot as an SVG file
plt.savefig('sample_plot.svg', format='svg')

# Show the plot (optional)
plt.show()
