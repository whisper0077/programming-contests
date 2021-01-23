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
    n = len(Ma[0])  # len(Mb)
    o = len(Mb[0])
    Mc = [[0]*o for _ in range(m)]
    for i in range(m):
        for k in range(n):
            for j in range(o):
                Mc[i][j] += Ma[i][k] * Mb[k][j]
    return Mc
