import fractions


def lcm(a, b):
    return a*b//fractions.gcd(a, b)


a, b, c, d = map(int, input().split())
e = lcm(c, d)
x = a if (a % c) == 0 else a-(a % c)+c
y = a if (a % d) == 0 else a-(a % d)+d
z = a if (a % e) == 0 else a-(a % e)+e
ans = b-a+1
if x <= b:
    ans -= (b-x)//c+1
if y <= b:
    ans -= (b-y)//d+1
if z <= b:
    ans += (b-z)//e+1
print(ans)
