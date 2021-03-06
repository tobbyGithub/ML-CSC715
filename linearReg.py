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
dataset = [[1, 7], [2,5], [3, 4], [4, 2], [5, 1],[9, 4], [4, 8], [5, 1],[5, 4], [4, 2], [5, 1]]
from math import sqrt
import numpy as np
'''
FUNCTIONS
'''
   
# a function that Calculates the mean value of a list of numbers by calculating the sum and dividing it by the total count 'n' of numbers
def mean(values):
	return sum(values) / float(len(values))


# this function calculates the variance of a list of numbers
def variance(values, mean):
	return sum([(x-mean)**2 for x in values])

# this function calculates the covariance between x and y which is (xi-X)*(yi-Y)
def covariance(valuesofx, valuesofy, meanX, meanY):
	covarianceValue = 0.0 #initiated zero accumulator
	for i in range(len(valuesofx)):
		covarianceValue += (valuesofx[i] - meanX) * (valuesofy[i] - meanY)
	return covarianceValue


# Calculate coefficients
def coefficientB1(dataset):
	x = [row[0] for row in dataset]
	y = [row[1] for row in dataset]
	x_mean, y_mean = mean(x), mean(y)
	b1 = covariance(x,  y, x_mean,y_mean) / variance(x, x_mean)
	return b1

def coefficientB0(b1,x_mean,y_mean):
	b0 = y_mean - b1 * x_mean
	return b0

# Simple linear regression algorithm
def simple_linear_regression(train, test):
	predictions = list()
	b1 = coefficientB1(train)
	x = [row[0] for row in train]
	y = [row[1] for row in train]
	x_mean, y_mean = mean(x), mean(y)
	b0 = coefficientB0(b1, x_mean, y_mean)
	for row in test:
		y_predict = b0 + b1 * row[0]
		predictions.append(y_predict)
	return predictions

# Calculate root mean squared error
def rmse_metric(actual, predicted):
	sum_error = 0.0
	for i in range(len(actual)):
		prediction_error = predicted[i] - actual[i]
		sum_error += (prediction_error ** 2)
	mean_error = sum_error / float(len(actual))
	return sqrt(mean_error)


# Evaluate regression algorithm on training dataset
def evaluate_algorithm(dataset, algorithm):
	test_set = list()
	for row in dataset:
		row_copy = list(row)
		row_copy[-1] = None
		test_set.append(row_copy)
	predicted = algorithm(dataset, test_set)
	print(predicted)
	actual = [row[-1] for row in dataset]
	rmse = rmse_metric(actual, predicted)
	return rmse

# ---------------FUNCTIONS END --------------------


#print out array(table of values) to confirm values
print('dataset content: \n ',dataset)
print()

#print out values of x and y
valuesofx=[row[0] for row in dataset]
print('values of x are ',valuesofx)
valuesofy=[row[1] for row in dataset]
print('values of y are ',valuesofy)

#print out sum of x and y
print('sum of x is',sum (valuesofx))
print('sum of y is',sum (valuesofy))
print('\n')

#print out mean of x and y
mean_x = mean(valuesofx)
mean_y = mean(valuesofy)
print('mean of x is',mean_x)
print('mean of y is',mean_y)

#print out variance of x and y
varianceX=variance(valuesofx, mean_x)
varianceY=variance(valuesofy, mean_y)
print('\n')

print('variance of x is %.3f' % varianceX)
print('variance of y is %.3f' % varianceY)
print('\n')
#print out covariance using the mean and values of x and y
covar = covariance(valuesofx, valuesofy , mean_x , mean_y)
print('Covariance: %.3f' % (covar))
print('\n')


# calculate coefficientss
b1 = coefficientB1(dataset)
b0 = coefficientB0(b1,mean_x,mean_y)
print('Coefficients: B0=%.3f, B1=%.3f' % (b0, b1))
print('\n')

rmse = evaluate_algorithm(dataset, simple_linear_regression)
print('RMSE: %.3f' % (rmse))


