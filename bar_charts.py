import matplotlib.pyplot as plt
import numpy as np

ext = {'exe': 3, 'ini': 1, 'jpg': 21, 'mp3': 2, 'png': 1, 'txt': 1, 'zip': 3}
height = ext.values()
bars = ext.keys()
y_pos = np.arange(len(bars))

# Create bars
plt.bar(y_pos, height)

# Create names on the x-axis
plt.xticks(y_pos, bars)

# Show graphic
plt.show()
