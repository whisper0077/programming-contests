N, M = map(int, input().split())
even = [2]*N
odd = [1]*M
a = even+odd
ans = 0
for i in range(N+M):
    for j in range(i+1, N+M):
        if (a[i]+a[j]) % 2 == 0:
            ans += 1
print(ans)
