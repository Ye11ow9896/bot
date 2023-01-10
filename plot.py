import numpy as np
import matplotlib.pyplot as plt
from db import SQLiteDB

#db = SQLiteDB() 
#table = db.get_database_table('database.sqlite')
#max = len(table)
#price_arr = [i for i in range(len(table))]
#date_arr = [i for i in range(len(table))]
#
#for i in range(len(table)):
#    price_arr[i] = table[i][2]
#    date_arr[i] += 1
#
#print(price_arr)
#print(date_arr)
#plt.hist(price_arr, bins = price_arr, edgecolor='black')
#
#plt.xlabel('Date')
#plt.ylabel('Price')
#plt.show()

np.random.seed(19680801)

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)
print(x)
# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=True, facecolor='g', alpha=0.75)
print(n)
print(bins)
print(patches)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')

plt.xlim(40, 160)
plt.ylim(0, 0.03)
plt.grid(True)
plt.show()