from sklearn import datasets
import pandas as p
import numpy as np
import matplotlib.pyplot as plt
# Import `train_test_split`
from sklearn.cross_validation import train_test_split
# Import
from sklearn.preprocessing import scale


# Load in the `digits` data
digits = datasets.load_digits()
# Print the `digits` data 
# print(digits.data)
data=scale(digits.data)
# print('the shape of scaled data is ', data.shape)


# Split the `digits` data into training and test sets
X_train, X_test, y_train, y_test, images_train, images_test = train_test_split(data, digits.target, digits.images, test_size=0.25, random_state=42)



# print out the training data of X values
print('the lenght of y_train', len(y_train))
print('the lenght of X_train',len(X_train))

# print out the training data of X values
print('the lenght of y_test',len(y_test))
print('the lenght of X_test',len(X_test))


# print out shape of X training data
print('the shape of X_train data is ',X_train.shape)
# print out shape of X training data
print('the shape of y_train data is ',y_train.shape)
# Number of unique Training labels
n_digits = len(np.unique(y_train))
print('the lenght of UNIQUE y_train',n_digits)

# Number of unique Training labels
m_digits = len(np.unique(X_train))
print('the lenght of UNIQUE X_train',m_digits)



# print out the training data of Y values
# # print(y_train)

# # print out the training data of X values
# print(X_train)

# # print the test data of X values
# # print(y_test)

# # print out the test data of X values
# print(X_test)

# # # print out the training data of Y values
# # print(X_train.shape)
# # Number of Training labels
# n_digits = len(np.unique(X_train))
# print(n_digits)
# print(len(y_train))
# print(len(X_train))
# print(len(y_test))
# print(len(X_test))

# print(images_train)
# # dataset=digits.images
# # print(digits.images)

# # Join th   e images and target labels in a list
# images_and_labels = list(zip(digits.images, digits.target))

# # for every element in the list
# for index, (image, label) in enumerate(images_and_labels[:8]):
#     # initialize a subplot of 2X4 at the i+1-th position
#     plt.subplot(2, 4, index + 1)
#     # Don't plot any axes
#     plt.axis('off')
#     # Display images in all subplots 
#     plt.imshow(image, cmap=plt.cm.gray_r,interpolation='nearest')
#     # Add a title to each subplot
#     plt.title('Training: ' + str(label))

# # Show the plot
# plt.show()