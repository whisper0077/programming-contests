N = int(input())
ab = [list(map(int, input().split())) for _ in range(N)]
ans = 10**10
for ai in range(N):
    for bi in range(N):
        if ai == bi:
            ans = min(ans, ab[ai][0]+ab[bi][1])
        else:
            ans = min(ans, max(ab[ai][0], ab[bi][1]))
print(ans)
