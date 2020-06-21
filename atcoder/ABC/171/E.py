N = int(input())
*a, = map(int, input().split())
b = 0
for v in a:
    b ^= v

a = [b ^ v for v in a]
print(*a)
