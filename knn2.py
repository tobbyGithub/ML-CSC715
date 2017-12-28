import numpy as np
from sklearn import datasets
iris = datasets.load_iris()

iris_data = iris.data
iris_labels = iris.target
# print(iris_data[0], iris_data[79], iris_data[100])
# print(iris_labels[0], iris_labels[79], iris_labels[100])
# print(iris_labels)
print(iris_data.head())