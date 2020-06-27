
class Combination:
    def __init__(self, n, mod):
        fact = [0]*(n+1)
        ifact = [0]*(n+1)
        fact[0] = 1
        for i in range(1, n+1):
            fact[i] = (fact[i-1]*i) % mod
        # 1/n!を逆元で求める
        ifact[n] = pow(fact[n], mod-2, mod)
        for i in range(n, 0, -1):
            ifact[i-1] = (ifact[i]*i) % mod

        self.n = n
        self.mod = mod
        self.fact = fact
        self.ifact = ifact

    def c(self, n, r):
        if r < 0 or r > n:
            return 0
        ret = (self.fact[n]*self.ifact[r]) % self.mod
        return (ret*self.ifact[n-r]) % self.mod

    def p(self, n, r):
        if n < r:
            return 0
        return self.fact[n]*self.ifact[n-r] % self.mod


MOD = 10**9+7
N, M = map(int, input().split())
c = Combination(M, MOD)
ans = 0
for i in range(N+1):
    a = (-1)**i * c.c(N, i)*c.p(M, i)*(c.p(M-i, N-i)**2) % MOD
    ans = (ans+a) % MOD
print(ans)
