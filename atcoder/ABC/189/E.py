import numpy as np
import sys
input = sys.stdin.readline

N = int(input())
xy = [np.array(list(map(int, input().split()))+[1]) for _ in range(N)]
M = int(input())
mm = [None]*(M+1)
mm[0] = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
op1 = np.array([
    [0, 1, 0],
    [-1, 0, 0],
    [0, 0, 1]
])
op2 = np.array([
    [0, -1, 0],
    [1, 0, 0],
    [0, 0, 1]
])
for i in range(M):
    op, *p = input().split()
    mat = None
    if op == "1":
        mat = op1
    elif op == "2":
        mat = op2
    elif op == "3":
        mat = np.array([
            [-1, 0, 2*int(p[0])],
            [0, 1, 0],
            [0, 0, 1]
        ])
    else:
        mat = np.array([
            [1, 0, 0],
            [0, -1, 2*int(p[0])],
            [0, 0, 1]
        ])
    mm[i+1] = np.dot(mat, mm[i])

Q = int(input())
for i in range(Q):
    a, b = map(int, input().split())
    b -= 1
    r = np.dot(mm[a], xy[b])
    print(r[0], r[1])
