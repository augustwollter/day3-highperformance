#!/usr/bin python
# Program to multiply two matrices using nested loops
import random
import numpy as np
def matrixMaker(N,M):
    X = np.random.random((N,M))
    return X

def main():
    N = 250
    X = matrixMaker(N,N)
    Y = matrixMaker(N,N+1)


    result = np.matmul(X, Y)
    return result
