import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("C:\\Users\\domin\\OneDrive - HTBLuVA St. "
                   "Pölten\\Labor\\5AHET\\05_Parametergenerator\\data\\sim_analog1.csv")
x = data[data.keys()[1]]
y = data[data.keys()[2]]

plt.plot(x, y)
plt.show()

