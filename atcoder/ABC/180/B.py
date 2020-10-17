N = int(input())
*x, = map(int, input().split())
a, b, c = 0, 0, 0
for i in range(N):
    v = abs(x[i])
    a += v
    b += v*v
    c = max(c, v)

b = b**0.5

print(a)
print(b)
print(c)
