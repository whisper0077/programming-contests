from collections import defaultdict
s = input().strip()
d = defaultdict(int)
for v in s:
    d[v] += 1

if len(d) == 2 and list(d.values())[0] == 2:
    print("Yes")
else:
    print("No")
