import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

customers = pd.read_csv("Customers.csv")
corr = (customers['Annual Income ($)'] / customers['Family Size']).corr(customers['Spending Score (1-100)'])
print(corr)

x = customers['Spending Score (1-100)']
y = customers['Annual Income ($)'] / customers['Family Size']
pd.DataFrame(np.array([x,y]).T).plot.scatter(0, 1, s=12, grid=True)

plt.ylabel('Доход на члена семьи')
plt.xlabel('Рейтинг трат')

plt.show()
