N, Y = map(int, input().split())
ans = [-1, -1, -1]
for m in range(N+1):
    for g in range(N+1):
        if (g+m) <= N:
            y = m*10000+g*5000
            s = (Y-y)//1000
            if s >= 0 and (m+g+s) == N:
                ans = [m, g, s]
                break
    if ans[0] != -1:
        break
print(*ans)
