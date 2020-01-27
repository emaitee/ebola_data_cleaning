import pandas as pd
import matplotlib.pyplot as plt

health_dt = pd.read_csv('resources/health_nga.csv')
# pd.read_csv(file_messy, delimiter=' ', header=3, comment='#')
health_dt.info()
health_dt.head()
health_dt.tail()

val_arr = health_dt.Value.values
len(val_arr)

health_dt.plot()
# plt.hist(val_arr, bins=1000)
plt.savefig('resources/health_dt.pdf')
plt.show()
