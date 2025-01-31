import numpy as np
import matplotlib.pyplot as plt 

def array2D_to_string(arr):
    return '\n'.join([' '.join([str(cell) for cell in row]) for row in arr])

