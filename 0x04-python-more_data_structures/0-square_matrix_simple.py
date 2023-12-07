#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
  """
  Computes the square value of all integers of a matrix.

  Args:
      matrix: A 2-dimensional list of integers.

  Returns:
      A new matrix with the same size as the input matrix,
      where each value is the square of the corresponding value in the input matrix.
  """

  new_matrix = []
  for row in matrix:
    new_row = []
    for value in row:
      new_row.append(value * value)
    new_matrix.append(new_row)
  return new_matrix
