import numpy as np 
import pandas as pd 

data = {
    'luas': np.arange(100,300,20),
    'harga': [500,665,720,795,885,1200,1500,1600,1775,2000]
}
df = pd.DataFrame(data)
# print(df)


# plotting
import matplotlib.pyplot as plt 
# plt.scatter(df['luas'], df['harga'])
# plt.show()


# linear regression
from sklearn import linear_model

## bikin model ML metode linear regression
model = linear_model.LinearRegression()

# Training model dengan data yg ada
# model.fit(dataindependent, dependent)
model.fit(df[['luas']], df['harga'])

m = model.coef_
c = model.intercept_
# print(m[0])
# print(c)

# print(model.predict([[ 100 ]]))
# print(model.predict([[ 3000 ]]))

print(model.predict(df[['luas']]))

plt.style.use('ggplot')
plt.plot(
    df['luas'], df['harga'], 'ro',
    df['luas'], model.predict(df[['luas']]), 'g-'
)
plt.grid(True)
plt.xlabel('Luas (m2)')
plt.ylabel('Harga (Rp)')
plt.legend(['Data', 'Best Fit Line'])
plt.show()

