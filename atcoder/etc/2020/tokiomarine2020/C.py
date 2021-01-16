from itertools import accumulate

N, K = map(int, input().split())
*A, = map(int, input().split())
for i in range(K):
    a = [0]*N
    allN = True
    for j in range(N):
        l, r = max(j-A[j], 0), (j+A[j]+1)
        a[l] += 1
        if r < N:
            a[r] -= 1
        if A[j] != N:
            allN = False
    A = list(accumulate(a))
    if allN:
        break

print(*A)
