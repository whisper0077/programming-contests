H, W = map(int, input().split())
N = int(input())
*a, = map(int, input().split())
m = [[-1]*(W+2) for _ in range(H+2)]

for i in range(1, H+1):
    for j in range(1, W+1):
        m[i][j] = 0

d = [0, 1]
c = [1, 0]
for i in range(N):
    for j in range(a[i]):
        if m[c[0]+d[0]][c[1]+d[1]] != 0:
            if d == [0, 1]:
                d = [1, 0]
            elif d == [1, 0]:
                d = [0, -1]
            elif d == [0, -1]:
                d = [-1, 0]
            else:
                d = [0, 1]
        c = [c[0]+d[0], c[1]+d[1]]
        m[c[0]][c[1]] = i+1

for i in range(H):
    print(*m[i+1][1:W+1])
