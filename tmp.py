N = int(input())
*A, = map(int, input().split())
m = [[0]*(N+2) for _ in range(N+2)]
for i in range(N):
    m[1][i+1] = A[i]

for y in range(2, N+1):
    for x in range(1, N+1):
        m[y][x] = m[y-1][x-1]+m[y-1][x]+m[y-1][x+1]
        m[y][x] %= 100
print(m[N][N])
