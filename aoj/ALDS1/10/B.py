n = int(input())
rc = [[0, 0]]+[list(map(int, input().split())) for i in range(n)]
m = [[0]*(n+1) for _ in range(n+1)]

for l in range(2, n+1):
    for i in range(1, n-l+2):
        j = i+l-1
        m[i][j] = 2**64
        for k in range(i, j):
            m[i][j] = min([
                m[i][j],
                m[i][k]+m[k+1][j]+rc[i][0]*rc[k+1][0]*rc[j][1]
            ])
print(m[1][n])
