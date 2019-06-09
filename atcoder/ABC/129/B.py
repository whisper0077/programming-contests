n = int(input())
*w, = map(int, input().split())
ans = 10**10
for i in range(n):
    a = abs(sum(w[:i]) - sum(w[i:]))
    if a < ans:
        ans = a
print(ans)