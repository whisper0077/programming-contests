from itertools import permutations

N, C = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(C)]
c = [list(map(int, input().split())) for _ in range(N)]

a = [[0]*(C+1) for _ in range(3)]
for y in range(N):
    for x in range(N):
        a[(x+1+y+1) % 3][c[y][x]] += 1

ans = 10**10
for nc in permutations(range(C), 3):
    ta = 0
    for i in range(3):
        for j in range(C):
            ta += D[j][nc[i]]*a[i][j+1]
    ans = min(ans, ta)

print(ans)
