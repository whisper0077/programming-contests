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
