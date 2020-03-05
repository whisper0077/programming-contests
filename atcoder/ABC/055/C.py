N, M = map(int, input().split())
if 2*N < M:
    k = (M-2*N)//4
    print(N+k)
else:
    print(M//2)
