def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


N = int(input())
ans = 1
for i in range(N):
    t = int(input())
    ans = lcm(ans, t)
print(ans)
