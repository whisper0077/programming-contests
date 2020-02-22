def cmb(n, r, mod):
    p, q = 1, 1
    for i in range(r):
        p *= n - i
        p %= mod
        q *= i + 1
        q %= mod
    # 1/q!の逆元をかける(= q! ^ (mod-2) % mod)
    return p * pow(q, mod - 2, mod)


N, a, b = map(int, input().split())
MOD = 10**9+7

print((pow(2, N, MOD) - cmb(N, a, MOD)-cmb(N, b, MOD)-1) % MOD)
