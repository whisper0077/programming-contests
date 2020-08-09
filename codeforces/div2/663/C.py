n = int(input())
MOD = 10**9+7
ans = 1
for i in range(1, n+1):
    ans = (ans*i) % MOD
for i in range(n-1):
    ans = (ans+MOD-pow(2, i, MOD)) % MOD
ans = (ans+MOD-1) % MOD
print(ans)
