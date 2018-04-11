import numpy as np
f1 = open('6.-.-.-.txt', 'r')
lines = f1.readlines()
#print alll rows
print(lines)

#print first row
print(lines[0])

#list to store column 3 items
stuffs=list()

#loop to iterate and pick items
for line in lines:
    columns = line.split()
    #print the 3column for u to see
    print (columns[2])
    #keep each item in the list of stuffs
    stuffs.append(columns[2])

#list of stuff
print('list content here!')
print(stuffs)
max_value = max(stuffs)
max_index = stuffs.index(max_value)
print('the max value in the column is', max_value)
print(max_value, 'lies in row', max_index+1)
index=int(max_index)
print('the row containing the max item is \n', lines[max_index])