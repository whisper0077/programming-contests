from collections import defaultdict


def nc2(n):
    return (n * (n - 1)) >> 1


n = int(input())
h = defaultdict(int)
for _ in range(n):
    h[input()[0]] += 1

ans = 0
for v in h.values():
    if v > 2:
        a = v // 2
        b = v - a
        ans += nc2(a) + nc2(b)
print(ans)
