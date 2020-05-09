K, N = map(int, input().split())
*A, = map(int, input().split())
A.append(A[0]+K)
ans = float('inf')
for i in range(N):
    a, b = A[i], A[i+1]
    ans = min(ans, K-(b-a))
print(ans)
