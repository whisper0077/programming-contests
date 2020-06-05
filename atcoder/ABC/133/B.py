import math
N, D = map(int, input().split())
xd = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        t = 0
        for k in range(D):
            t += pow(xd[i][k]-xd[j][k], 2)
        t = math.sqrt(t)
        if t == float(int(t)):
            ans += 1
print(ans)
