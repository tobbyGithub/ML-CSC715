# numpy
import numpy as np
# matplotlib
import matplotlib
# pandas
import pandas as pd
# scikit-learn
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv("https://raw.githubusercontent.com/datascienceinc/learn-data-science/master/Introduction-to-K-means-Clustering/Data/data_1024.csv")
# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
# names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
# df = pd.read_csv(url, names=names)
# df.columns = [‘X1’, ‘X2’, ‘X3’, ‘X4’, ‘Y’]
# df = df.drop([‘X4’, ‘X3’], 1)
# df.head()

print(df.head())