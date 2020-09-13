MOD = 10**9+7
S = int(input())
if S < 3:
    print(0)
elif S <= 5:
    print(1)
else:
    d = [0]*2001
    for i in range(6):
        d[i] = 1
    for i in range(6, S+1):
        for j in range(3, i-3+1):
            d[i] += d[i-j]
            d[i] %= MOD
        d[i] = (d[i]+1) % MOD
    print(d[S])
