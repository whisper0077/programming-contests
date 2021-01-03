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


n = int(input())
ans = []
for p in primes(55555):
    if p % 10 == 1 and len(ans) < n:
        ans.append(p)
print(*ans)
