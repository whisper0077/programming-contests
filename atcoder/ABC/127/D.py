N, M = map(int, input().split())
*A, = map(int, input().split())
BC = [list(map(int, input().split())) for _ in range(M)]
A.sort()
BC.sort(key=lambda v: -v[1])

ai = 0
for b, c in BC:
    while b > 0 and ai < N and A[ai] < c:
        A[ai] = c
        b -= 1
        ai += 1

print(sum(A))