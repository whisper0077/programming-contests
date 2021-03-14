def primes(n):
    # n以下の素数列挙(O(n log(n))
    ass = []
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    for i in range(len(is_prime)):
        if is_prime[i]:
            ass.append(i)
    return ass


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


N = int(input())
*X, = map(int, input().split())
p = primes(50)
ans = 10**18
for i in range(2**len(p)):
    t = 1
    for j in range(len(p)):
        if (1 << j) & i > 0:
            t *= p[j]

    ok = True
    for x in X:
        if gcd(x, t) == 1:
            ok = False
            break
    if ok:
        ans = min(t, ans)

print(ans)
