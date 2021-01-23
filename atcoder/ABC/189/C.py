N = int(input())
*A, = map(int, input().split())
ans = 0
for i in range(N):
    m = A[i]
    for j in range(i, N):
        m = min(m, A[j])
        ans = max(ans, m*(j-i+1))
print(ans)
