from collections import defaultdict
from itertools import combinations

N = int(input())
S = [list(input()) for _ in range(N)]

h = defaultdict(int)
for s in S:
    if s[0] in "MARCH":
        h[s[0]] += 1

ans = 0
for a, b, c in combinations(list("MARCH"), 3):
    ans += h[a]*h[b]*h[c]

print(ans)
