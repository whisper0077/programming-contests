# queue
# round-robin scheduler
n, q = map(int, input().split())
l = []
for i in range(n):
    v = input().split()
    l.append([v[0], int(v[1])])

ans = []
t = 0
while len(l) > 0:
    v = l.pop(0)
    v[1] -= q
    if v[1] <= 0:
        t += q+v[1]
        ans.append([v[0], str(t)])
    else:
        t += q
        l.append(v)

for v in ans:
    print(" ".join(v))
