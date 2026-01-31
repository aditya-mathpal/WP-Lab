'''
3. Write a python program to multiply two matrices
'''

import numpy as np

def mat_product(matA, matB):
    m, n = len(matA), len(matB)
    res = [[0]*m for i in range(m)]
    for i in range(m):
        for j in range(m):
            for k in range(n):
                res[i][j] += matA[i][k] * matB[k][j]
    return res

def read_mat_input(mat):
    m, n = len(mat), len(mat[0])
    for i in range(m):
        mat[i] = list(map(int, input().split()))


m, n = list(map(int, input("Enter dimensions of matrix A: ").split()))
o, p = list(map(int, input("Enter dimensions of matrix B: ").split()))
if m != p or n != o:
    print("Enter valid dimensions")
    raise SystemExit(1)

matA = [[0]*n for i in range(m)]
matB = [[0]*m for i in range(n)]

print("Enter elements of matrix A:")
read_mat_input(matA)
print("Enter elements of matrix B:")
read_mat_input(matB)

print("matA x matB =\n",np.array(mat_product(matA, matB)))

'''
output:
Enter dimensions of matrix A: 2 3
Enter dimensions of matrix B: 3 2
Enter elements of matrix A:
1 2 3
4 5 6
Enter elements of matrix B:
10 11
20 21
30 31
matA x matB =
 [[140 146]
 [320 335]]
'''