import pandas as pd
from sklearn import datasets, cross_validation
import matplotlib.pyplot as plt
import sklearn

data=datasets.load_boston()
# define the data/predictors as the feature names  
df = pd.DataFrame(data.data, columns=data.feature_names)

# print(df.groupby('AGE').size())
# Put the target (housing value -- MEDV) in another DataFrame
# target = pd.DataFrame(data.target, columns=["MEDV"])
df['PRICE'] = data.target
X = df.drop('PRICE', axis = 1)
Y = df['PRICE']
X_train, X_test, Y_train, Y_test = sklearn.cross_validation.train_test_split(X, Y, test_size = 0.33, random_state = 5)
# print(X_train.shape)
# print(X_test.shape)
# print(Y_train.shape)
# print(Y_test.shape)
from sklearn.linear_model import LinearRegression

lm = LinearRegression()
lm.fit(X_train, Y_train)

Y_pred = lm.predict(X_test)

plt.scatter(Y_test, Y_pred)
plt.xlabel("Prices: Ytest")
plt.ylabel("Predicted prices: Ypredict")
plt.title("Prices vs Predicted prices: Ytest vs Ypredict")
# 

mse = sklearn.metrics.mean_squared_error(Y_test, Y_pred)
print(mse)

# df.plot(x='CRIM', y='PRICE', kind='scatter')
# print(target.head())
# print(data.target.shape)
# print(df.describe)