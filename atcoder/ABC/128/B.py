n = int(input())
r = []
for i in range(n):
    s, v = input().split()
    r.append([s, -int(v), i + 1])

for s, v, c in sorted(r):
    print(c)
