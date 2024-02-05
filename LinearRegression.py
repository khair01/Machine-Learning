import pandas as pd
import matplotlib.pyplot as mt

data = pd.read_csv('Salary_Data.csv')
mt.scatter(data.YearsExperience, data.Salary, color='red')
mt.title('Salary vs Experience')
mt.xlabel('Years of Experience')
mt.ylabel('Salary')

def Gradient_Descent(m, b, data, L):
    m_gradient = 0
    b_gradient = 0
    for i in range(len(data)):
        x = data.iloc[i].YearsExperience
        y = data.iloc[i].Salary
        
        m_gradient += -(2/len(data)) * x * (y - (m * x + b))
        b_gradient += -(2/len(data)) * (y - (m * x + b))
        
    newm = m - m_gradient * L
    newb = b - b_gradient * L
    return newm, newb

m = 0
b = 0
L = 0.01 # Learning Rate
Iterations = 1000

for i in range(Iterations):
    m, b = Gradient_Descent(m, b, data, L)

# m = 9449.962321455077
# b = 25792.20019866869
print("Calculated m:", m)
print("Calculated b:", b)

x_range = range(int(min(data.YearsExperience)), int(max(data.YearsExperience)) + 1)
mt.scatter(data.YearsExperience, data.Salary, color='red')
mt.title('Salary vs Experience')
mt.xlabel('Years of Experience')
mt.ylabel('Salary')
mt.plot(x_range, [m * x + b for x in x_range], color='black')

mt.show()
