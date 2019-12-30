from fractions import gcd

n1, d1 = map(int, input().split())
p = input()
n2, d2 = map(int, input().split())

n = 1
d = 1
if p == '+':
    n = n1 * d2 + n2 * d1
    d = d1 * d2

elif p == '-':
    n = n1 * d2 - n2 * d1
    d = d1 * d2

elif p == '*':
    n = n1 * n2
    d = d1 * d2

elif p == '/':
    n = n1 * d2
    d = d1 * n2

while gcd(n, d) > 1:
    g = gcd(n, d)
    n = n // g
    d = d // g

if d == 1:
    print(n)
else:
    print(n, d)
