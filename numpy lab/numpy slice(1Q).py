#Q1.Write a NumPy program to creat an array of 10 zeros, 10 ones and fives.?

#sample output:
#An array of 10 zeros:
#[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#An array of ten ones:
#[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
#An array of 10 fives:
#[5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]

import numpy as np

zeros_array = np.zeros(10)
# Create an array with 10 zeros
print(f' An array of 10 zeros', zeros_array)
# Create an array with 10 onces
ones_array = np.ones(10)
print(f'An array of ten ones', ones_array)
# Create an array with 10 fives.
fives_array = np.full(10, 5)
print(f'An array of ten ones', fives_array)
