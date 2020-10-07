# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 19:57:57 2019

@author: 75614
"""

# -*- coding: utf-8 -*-
"""
@author: MachineRandy
"""
"""
该程序仅仅做测试使用，不属于作业
"""
import numpy as np
import warnings
#from Q_2 import *
warnings.filterwarnings("ignore")


"""
AX = B
"""

A = [
    [4,2,-4,0,2,4,0,0],
    [2,2,-1,-2,1,3,2,0],
    [-4,-1,14,1,-8,-3,5,6],
    [0,-2,1,6,-1,-4,-3,3],
    [2,1,-8,-1,22,4,-10,-3],
    [4,3,-3,-4,4,11,1,-4],
    [0,2,5,-3,-10,1,14,2],
    [0,0,6,3,-3,-4,2,19],
]

B = [0,-6,6,23,11,-22,-15,45]

"""
def sor(A,B,sigma,N,omg):
    n = len(A)
    x0 = []
    x = []
    for i in range(0,n):
        x0.append(0)
        x.append(0)
    for index in range(1,N+1):
        R = 0
        for i in range(0,n):
            s_x = 0
            for j in range(0,n):
                if j >= i:
                    s_x = s_x + A[i][j] * x0[j]
                else:
                    s_x = s_x + A[i][j] * x[j]
            x[i] = x0[i] + omg * ((B[i] - s_x)/A[i][i])
            if abs(x[i] - x0[i]) > R:
                R = abs(x[i] - x0[i])
        if R <= sigma:
            print("Accuracy = ",sigma,",  W0 = ",omg,",  iter = ",index)
            print(x)
            return (x,index)
        for i in range(0,n):
            x0[i] = x[i]
    return (x,index)
"""
def Sor(A,B,sigma = 0.01,N = 1000,omg = 0.5):
    n = len(A)
    x = [0]*n
    x_init = [0]*n
    for index in range(1,N+1):
        flag = 0
        for i in range(0,n):
            s_x = 0
            for j in range(0,n):
                if j >= i:
                    s_x = s_x + A[i][j] * x_init[j]
                else:
                    s_x = s_x + A[i][j] * x[j]
            x[i] = x_init[i] + omg * ((B[i] - s_x)/A[i][i])
            if abs(x[i] - x_init[i]) > flag:
                flag = abs(x[i] - x_init[i])
        if flag <= sigma:
            print("Accuracy = ",sigma,",  W0 = ",omg,",  iter = ",index)
            print("solve_X = %s"%(x))
            return (x,index)
        for i in range(0,n):
            x_init[i] = x[i]
        x = np.array(x)
    return x,index

x,index = Sor(A,B,0.001,2000,0.8)
Sor(A,B,0.001,2000,0.9)
Sor(A,B,0.001,2000,1)
Sor(A,B,0.001,2000,1.1)
Sor(A,B,0.001,2000,1.2)

