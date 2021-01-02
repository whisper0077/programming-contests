from collections import defaultdict
n = int(input())
h = defaultdict(int)

for i in range(n):
    s = input().strip()
    h[s] += 1

ans = "satisfiable"
for k in h.keys():
    if "!"+k in h:
        ans = k
print(ans)
