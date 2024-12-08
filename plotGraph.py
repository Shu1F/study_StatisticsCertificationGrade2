import matplotlib.pyplot as plt

data = [15, 19, 21, 22, 25, 28, 33, 42, 48]

plt.hist(data, bins=5, range=(0, 50), alpha=0.9)
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
