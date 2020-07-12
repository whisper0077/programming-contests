from collections import defaultdict
N = int(input())
c = defaultdict(int)
for i in range(N):
    a = int(input())
    c[a] ^= 1
print(list(c.values()).count(1))
