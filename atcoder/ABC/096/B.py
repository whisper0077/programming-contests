a, b, c = map(int, input().split())
k = int(input())
d = max(a, b, c)
r = sum([a, b, c])-d
for i in range(k):
    d = d << 1
print(d+r)
