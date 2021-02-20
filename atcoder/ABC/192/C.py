N, K = map(int, input().split())
a = N
for i in range(K):
    s = sorted(list(str(a)))
    g2 = int("".join(s))
    g1 = int("".join(reversed(s)))
    a = g1-g2
print(a)
