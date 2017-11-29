'''
CODE TO CALCULATE SIMPLE LINEAR REGRESSION ON DATASET WITH JUST 2 VARIABLES
SAY X. Y with values given in the table below

x | y
-----
1 | 2
2 | 3
4 | 3
3 | 2
5 | 5
------
'''


#generate our dataset using a series  of random values say:
dataset = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]

#cast the dataset into a numpy array
import numpy as np
dataset_numpy= np.array(dataset)

#print out array(table of values) to confirm values
print(dataset_numpy)

#print out values of x
print([row[0] for row in dataset])

#print out values of y
valuesofx=[row[1] for row in dataset]
print(valuesofx)

sum(values) / (len(values))

# a function that Calculates the mean value of a list of numbers by calculating the sum and dividing it by the total count 'n' of numbers
def mean(values):
	return sum(values) / (len(values))


# Calculate the variance of a list of numbers
def variance(values, mean):
	return sum([(x-mean)**2 for x in values])
 
# # calculate mean and variance
# x = [row[0] for row in dataset]
# y = [row[1] for row in dataset]
# mean_x, mean_y = mean(x), mean(y)
# var_x, var_y = variance(x, mean_x), variance(y, mean_y)
# print('x stats: mean=%.3f variance=%.3f' % (mean_x, var_x))
# print('y stats: mean=%.3f variance=%.3f' % (mean_y, var_y))


# # Calculate covariance between x and y
# def covariance(x, mean_x, y, mean_y):
# 	covar = 0.0
# 	for i in range(len(x)):
# 		covar += (x[i] - mean_x) * (y[i] - mean_y)
# 	return covar




# # calculate covariance
# dataset = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]
# x = [row[0] for row in dataset]
# y = [row[1] for row in dataset]
# mean_x, mean_y = mean(x), mean(y)
# covar = covariance(x, mean_x, y, mean_y)
# print('Covariance: %.3f' % (covar))





# # Calculate coefficients
# def coefficients(dataset):
# 	x = [row[0] for row in dataset]
# 	y = [row[1] for row in dataset]
# 	x_mean, y_mean = mean(x), mean(y)
# 	b1 = covarianxce(x, x_mean, y, y_mean) / variance(x, x_mean)
# 	b0 = y_mean - b1 * x_mean
# 	return [b0, b1]


# # calculate coefficients
# dataset = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]
# b0, b1 = coefficients(dataset)
# print('Coefficients: B0=%.3f, B1=%.3f' % (b0, b1))
