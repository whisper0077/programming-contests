N, M = map(int, input().split())
if N > M:
    N, M = M, N
ans = 0
if N == 1:
    if M == 1:
        ans = 1
    else:
        ans = M-2
else:
    ans = (N-2)*(M-2)
print(ans)
