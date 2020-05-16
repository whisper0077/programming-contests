N, M = map(int, input().split())
MOD = 10**9+7
d = abs(N-M)
if d > 1:
    print(0)
else:
    ans = 1
    for i in range((N+M)//2):
        ans *= (N-i)*(M-i)
        ans %= MOD
    if (N+M) % 2 == 0:
        ans *= 2
    print(ans % MOD)
