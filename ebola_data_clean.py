import pandas as pd
import matplotlib.pyplot as plt

# Playing with the ebola dataset
ebola = pd.read_csv('resources/ebola_data_db_format.csv')
ebola.info()
ebola.describe()

countries = ebola['Country'].values
val = ebola.value.values

plt.scatter(val,countries,color='red')
plt.xlabel('value')
plt.ylabel('countries')
plt.title('Ebola Virus Data Analysis')
plt.savefig('resources/ebola_analysis.pdf')
plt.show()

