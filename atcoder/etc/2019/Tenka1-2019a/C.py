n = int(input())
s = list(input())
d = [0]*n
p = [0]*n
for i in range(n):
    if i > 0:
        d[i] = d[i-1]
    if s[i] != '.':
        d[i] += 1
for i in range(n-1, -1, -1):
    if i < (n-1):
        p[i] = p[i+1]
    if s[i] != '#':
        p[i] += 1

d = [0]+d
p = p+[0]
ans = 2**32
for i in range(n+1):
    t = d[i]+p[i]
    if t < ans:
        ans = t
print(ans)
