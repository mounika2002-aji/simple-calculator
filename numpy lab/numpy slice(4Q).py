#Q4.Write a NumPy program to convert a list and tuple into arrays.

#input:my_list = ([1,2,3,4,5,6,7,8])

#input:my_tuple = ([8,4,6], [1,2,3])

import numpy as np

# Input list and tuple
my_list = ([1,2,3,4,5,6,7,8])
my_tuple = ([8, 4, 6], [1, 2, 3])
# Convert the list and tuple into arrays
array_from_list = np.array(my_list)
print('Array from list:',array_from_list)
array_from_tuple = np.array(my_tuple)
print('Array from tuple:',array_from_tuple)





