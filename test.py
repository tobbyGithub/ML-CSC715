# Load CSV using Pandas from URL
import pandas
import numpy
import matplotlib


# basic line plot
import matplotlib.pyplot as plt
url = "https://goo.gl/vhm1eU"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataset = pandas.read_csv(url, names=names)
print(dataset.groupby('class').size())

# # histograms
# dataset.hist()
# plt.show()


# # scatter plot matrix
# scatter_matrix(dataset)
# plt.show()
# print(data.shape)
# description = data.describe()
# theHead= data.head()
# print('the head is')
# print(theHead)
# Numpy_array=numpy.array(data)
# print(numdata)
# print('---------')
# print(data)
# X = Numpy_array[0:10,8]
# Y = Numpy_array[0:10,0]
# print(Y)
#use the pandas value attribute 
# array = dataset.values
# # convert the array into a numpy array
# Numpy_array = numpy.a
# print(myarray.shape)
# Describe your dataset using Pandas
# plt.plot(Numpy_array)
# plt.scatter(X,Y)
# plt.xlabel('x axis')
# plt.ylabel('y axis')
# plt.show()





