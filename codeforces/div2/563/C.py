import math
n = int(input())

primes = {2: True}
for v in range(3, n + 1):
    a = 2
    b = False
    while a <= int(math.sqrt(v) + 1):
        if v % a == 0:
            b = True
            break
        a += 1
    if not b:
        primes[v] = True

ans = [0] * (n + 1)
for i, p in enumerate(primes):
    if p > (n + 1):
        break
    for j in range(0, n + 1, p):
        if ans[j] == 0:
            ans[j] = i + 1

ans = ans[2:]
print(" ".join([str(v) for v in ans]))
