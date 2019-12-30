N, Q = map(int, input().split())
*A, = map(int, input().split())
for i in range(Q):
    x, y = map(int, input().split())
    for j in range(N):
        if A[j] == x:
            A[j] = y

print(sum(A))