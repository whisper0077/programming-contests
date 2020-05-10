class combination:
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

    def choose(self, n, r):
        if r < 0 or r > n:
            return 0
        ret = (self.fact[n]*self.ifact[r]) % self.mod
        return (ret*self.ifact[n-r]) % self.mod


MOD = 998244353
N, M, K = map(int, input().split())
c = combination(N, MOD)

ans = 0
for k in range(K+1):
    ncr = c.choose(N-1, k) if k > 0 else 1
    t = ncr*M*pow(M-1, N-k-1, MOD)
    ans = (ans+t) % MOD
print(ans)
