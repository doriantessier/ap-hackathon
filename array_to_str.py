import numpy as np


def array2D_to_string(arr):
    return '\n'.join([' '.join([str(cell) for cell in row]) for row in arr])

