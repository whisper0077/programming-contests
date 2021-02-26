def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


N = int(input())
*a, = map(int, input().split())

l = 1
for i in range(N):
    l = lcm(l, a[i])

print(sum([(l-1) % v for v in a]))
