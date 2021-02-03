import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('countries.csv')             #data for population of most countries : '52 - '07
us = data[data.country == 'United States']
china = data[data.country == 'China']

plt.figure('Data Visualization')
plt.plot(us.year, (us.population / us.population.iloc[0])*100)              #plot us and china by percentage growth (year '0' being 100%)
plt.plot(china.year, (china.population / china.population.iloc[0])*100)

plt.title('Population Comparison - US v China')                             #formatting
plt.legend(['United States', 'China'])
plt.xlabel('year')
plt.ylabel('population growth')
plt.show()


