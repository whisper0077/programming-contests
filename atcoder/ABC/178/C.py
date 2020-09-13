MOD = 10**9+7
N = int(input())
if N < 2:
    print(0)
else:
    ans = pow(10, N, MOD)
    ans = ans - pow(9, N, MOD)*2+pow(8, N, MOD)
    print(ans % MOD)
