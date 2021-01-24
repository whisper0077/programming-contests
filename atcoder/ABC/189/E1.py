import sys
input = sys.stdin.readline


def mulv(Ma, v):
    m = len(Ma)
    n = len(v)
    w = [0] * m
    for i in range(m):
        s = 0
        for k in range(n):
            s += Ma[i][k] * v[k]
        w[i] = s
    return w


def mulm(Ma, Mb):
    m = len(Ma)
    l = len(Ma[0])  # == len(Mb)
    n = len(Mb[0])
    Mc = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            for k in range(l):
                Mc[i][j] += Ma[i][k] * Mb[k][j]
    return Mc


N = int(input())
xy = [list(map(int, input().split()))+[1] for _ in range(N)]
M = int(input())
mm = [[[1, 0, 0], [0, 1, 0], [0, 0, 1]]]
for i in range(M):
    op, *p = input().split()
    mat = None
    if op == "1":
        mat = [
            [0, 1, 0],
            [-1, 0, 0],
            [0, 0, 1]
        ]
    elif op == "2":
        mat = [
            [0, -1, 0],
            [1, 0, 0],
            [0, 0, 1]
        ]
    elif op == "3":
        mat = [
            [-1, 0, 2*int(p[0])],
            [0, 1, 0],
            [0, 0, 1]
        ]
    else:
        mat = [
            [1, 0, 0],
            [0, -1, 2*int(p[0])],
            [0, 0, 1]
        ]
    mm.append(mulm(mat, mm[-1]))

Q = int(input())
for i in range(Q):
    a, b = map(int, input().split())
    b -= 1
    r = mulv(mm[a], xy[b])
    print(*r[:2])
