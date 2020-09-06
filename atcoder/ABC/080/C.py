N = int(input())
f = [list(map(int, input().split())) for _ in range(N)]
p = [list(map(int, input().split())) for _ in range(N)]

ans = -float('inf')
for i in range(1, 2**10):
    t = [1 if i & (1 << j) != 0 else 0 for j in range(10)]
    b = 0
    for j in range(N):
        c = 0
        for k in range(10):
            if t[k] == 1 and f[j][k] == 1:
                c += 1
        b += p[j][c]
    ans = max(ans, b)
print(ans)
