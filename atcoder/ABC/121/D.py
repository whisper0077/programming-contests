a, b = map(int, input().split())
if a > 0:
    a -= 1

ax = [a, 1, a + 1, 0][a % 4]
bx = [b, 1, b + 1, 0][b % 4]

print(ax ^ bx)