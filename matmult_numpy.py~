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

    # result is Nx(N+1)
    # result = np.zeros((N,N+1))
    # for i in range(N):
    #     # iterate through rows of X
    #     for i in range(len(X)):
    #         # iterate through columns of Y
    #         for j in range(len(Y[0])):
    #             # iterate through rows of Y
    #             for k in range(len(Y)):
    #                 result[i][j] += X[i][k] * Y[k][j]
                    
    return result
