import pandas as pd
import matplotlib.pyplot as plt

health_dt = pd.read_csv('health_nga.csv')
# pd.read_csv(file_messy, delimiter=' ', header=3, comment='#')
health_dt.info()
health_dt.head()
health_dt.tail()

val_arr = health_dt.Value.values
len(val_arr)

health_dt.plot()
# plt.hist(val_arr, bins=1000)
plt.show()
plt.savefig('health_dt.jpg')

# Playing with the ebola dataset
ebola = pd.read_csv('ebola_data_db_format.csv')
ebola.info()
ebola.describe()

countries = ebola['Country'].values
val = ebola.value.values

plt.scatter(val,countries,color='red')
plt.xlabel('value')
plt.ylabel('countries')
plt.title('Ebola Virus Data Analysis')
plt.savefig('ebola_analysis.pdf')
plt.show()

