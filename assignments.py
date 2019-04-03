# https://github.com/bmc/munkres
from munkres import Munkres, print_matrix
import numpy as np

matrix = [[0,0,-1,-1,-3,-3,0,0,0,0,-2,-2],
          [0,0,0,0,0,0,-1,-1,-2,-2,-3,-3],
          [-3,-2,0,0,0,0,0,0,-1,-1,0,0],
          [0,-2,0,0,-3,-3,-1,-1,0,0,0,0],
          [-1,0,0,0,0,0,-3,-3,0,0,-2,-2],
          [0,0,-1,-1,0,0,-3,-3,-2,-2,0,0],
          [-2,-3,-1,-1,0,0,0,0,0,0,0,0]]

matrix2 = [[-3, -2, -1 , 0, 0],
          [0, -2, -3, -1, 0],
          [-1, -3, -2, 0, 0],
          [0, -2, 0, -3, -1],
          [0, -1, -3, 0, -2]]

matrix3 = [[-3,-2,-1,0],
		   [-3,-2,-1,0],
		   [-3,-2,-1,0],
		   [-3,-2,-1,0]]

m = Munkres()

indexes = m.compute(matrix3)
print_matrix(matrix3, msg='Lowest cost through this matrix:')
total = 0
for row, column in indexes:
    value = matrix[row][column]
    total += value
    print('({}, {}) -> {}'.format(row, column, value))
print('total cost: {}'.format(total))