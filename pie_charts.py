from matplotlib import pyplot as plt

ext = {'exe': 3, 'ini': 1, 'jpg': 21, 'mp3': 2, 'png': 1, 'txt': 1, 'zip': 3}

# Creating dataset
extensions = ext.keys()

data = ext.values()

# Creating plot
fig = plt.figure(figsize=(7, 6))
plt.pie(data, labels=extensions)

# show plot
plt.show()
