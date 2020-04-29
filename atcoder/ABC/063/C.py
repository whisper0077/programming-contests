N = int(input())
s = [int(input()) for _ in range(N)]
ns = []
for v in s:
    if v % 10 != 0:
        ns.append(v)
ns.sort()

ans = sum(s)
while ans % 10 == 0 and len(ns) > 0:
    ans -= ns.pop(0)
print(0 if ans % 10 == 0 else ans)
