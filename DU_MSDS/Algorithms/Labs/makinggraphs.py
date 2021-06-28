import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create the vectors X and Y
sample = pd.read_csv("Time_Panda.csv")
plt.scatter(sample['Bits'], sample['Time_2_Factor'])

x = np.array(range(10))
y = x ** 2

# Create the plot
plt.plot(x, y, label='y = x**2')
plt.plot(x,* y + 7,label='y = (1/2) * (x**2) + 7')


# Add a title
plt.title('Time in Milliseconds to Crack Code by key bit size')

# Add X and y Label
plt.xlabel('x axis')
plt.ylabel('y axis')

# Add a grid
plt.grid(alpha=.4, linestyle='--')

# Add a Legend
plt.legend()

# Show the plot
plt.show()