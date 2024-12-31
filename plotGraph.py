import matplotlib.pyplot as plt
import numpy as np


# data = [15, 19, 21, 22, 25, 28, 33, 42, 48]

# plt.hist(data, bins=5, range=(0, 50), alpha=0.9)
# plt.title("Histogram")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.show()

# data = [44, 47, 58, 42, 60, 22, 44, 52, 75, 51, 50, 65, 53, 54, 49]

# plt.boxplot(data)

# plt.show()

# data_tokyo = [21, 22, 22, 23, 23, 24, 24, 24, 25, 26]
# data_nagoya = [24, 25, 25, 25, 26, 26, 26, 27, 27, 28]
# data_osaka = [22, 22, 23, 23, 24, 24, 25, 26, 26, 27]
# data_hokkaido = [18, 18, 19, 19, 20, 20, 20, 21, 22, 23]
# data_fukuoka = [24, 25, 26, 26, 27, 27, 27, 28, 28, 29]

# ave_tokyo = sum(data_tokyo) / len(data_tokyo)
# ave_osaka = sum(data_osaka) / len(data_osaka)
# ave_nagoya = sum(data_nagoya) / len(data_nagoya)
# ave_hokkaido = sum(data_fukuoka) / len(data_fukuoka)

# print(ave_tokyo)
# print(ave_hokkaido)
# print(ave_nagoya)
# print(ave_osaka)

# data = [45, 50, 43, 62, 56, 52, 39, 53]

# data_ave = sum(data) / len(data)

# data_var = np.var(data)

# print(data_var)

# data_devitation = np.std(data)
# print(data_devitation)

# data = [4, 5, 2, 3, 7]

# data_devitation = np.std(data)
# print(data_devitation)


import numpy as np
import polars as pl
import plotly.express as px
import scipy
import plotly.io as pio

pio.templates.default = "none"

data1 = pl.read_csv(
    "https://drive.google.com/uc?export=download&id=1lbvFBOLK0irG3hWj3Q6RYnd4ugcyZFJw"
)
data2 = pl.read_csv(
    "https://drive.google.com/uc?export=download&id=19foMWN1GSzRNacVYBVGGR9pfEyhBU4LN"
)
data3 = pl.read_csv(
    "https://drive.google.com/uc?export=download&id=1HHUl9hMeXQIHQKndJyt2BebTXZFCDuQK"
)

data1.describe()
