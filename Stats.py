import statistics as st
import pandas as pd

data = pd.read_csv('Salary_Data.csv')
x = data['YearsExperience']
y = data['Salary']

x_mean = st.mean(x)
y_mean = st.mean(y)

# Calculating Deviations of x
x_dev = []

for i in range(len(x)):
    x_dev.append(x[i] - x_mean)

# Calculating Deviations of y
y_dev = []

for i in range(len(y)):
    y_dev.append(y[i] - y_mean)

dev_prod = []

for i in range(len(x)):
    dev_prod.append(x_dev[i] * y_dev[i])

sum_dev_prod = 0

for i in range(len(x)):
    sum_dev_prod += dev_prod[i]

sum_x_dev_squared = 0

for i in range(len(x)):
    sum_x_dev_squared += x_dev[i] ** 2
    
m = sum_dev_prod/sum_x_dev_squared


b = y_mean - (m * x_mean)
print(m)
print(b)
