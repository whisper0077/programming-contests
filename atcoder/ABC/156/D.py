def cmb(n, r):
    if n - r < r:
        r = n - r
    if r == 0:
        return 1
    if r == 1:
        return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2, r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1, r, p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])
            result %= M

    return result


def pow(x, n):
    ans = 1
    while(n > 0):
        if(bin(n & 1) == bin(1)):
            ans = (ans*x) % M
        x = (x*x) % M
        n = n >> 1
    return ans


N, a, b = map(int, input().split())
M = 10**9+7

print((pow(2, N) - cmb(N, a)-cmb(N, b)-1) % M)
