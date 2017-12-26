# numpy
import numpy as np
# matplotlib
import matplotlib
# pandas
import pandas as pd
# scikit-learn
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
df.columns = [‘X1’, ‘X2’, ‘X3’, ‘X4’, ‘Y’]
df = df.drop([‘X4’, ‘X3’], 1)
df.head()