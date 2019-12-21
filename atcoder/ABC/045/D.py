from collections import defaultdict

H, W, N = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N)]
h = defaultdict(int)
for a, b in ab:
    for y in range(max([a - 2, 1]), min([a, H - 2]) + 1):
        for x in range(max([b - 2, 1]), min([b, W - 2]) + 1):
            h[(y, x)] += 1

ans = [0] * 10
for v in h.values():
    ans[v] += 1
ans[0] = (H - 2) * (W - 2) - sum(ans[1:])

for a in ans:
    print(a)