import bisect
N, M, K = map(int, input().split())
*A, = map(int, input().split())
*B, = map(int, input().split())

for i in range(1, N):
    A[i] += A[i-1]
for i in range(1, M):
    B[i] += B[i-1]

A = [0]+A
B = [0]+B
j = M
ans = 0
for i in range(N+1):
    k = K-A[i]
    if k < 0:
        break
    while B[j] > k:
        j -= 1
    ans = max(ans, i+j)

print(ans)
'''
for i in range(1, N):
    A[i] += A[i-1]
for i in range(1, M):
    B[i] += B[i-1]

A = [0]+A
ans = 0
for i in range(N+1):
    b = K-A[i]
    if b < 0:
        break
    j = bisect.bisect_right(B, b)
    if ans < (i+j):
        ans = i+j

print(ans)
'''
