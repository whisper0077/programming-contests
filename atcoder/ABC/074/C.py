A, B, C, D, E, F = map(int, input().split())
a, b = [], []

for i in range(31):
    for j in range(31):
        v = 100*A*i+100*B*j
        if v < F:
            a.append(v)
        else:
            break

for i in range(3000//C+2):
    for j in range(3000//D+2):
        v = C*i+D*j
        if v < F:
            b.append(v)
        else:
            break

a.sort()
b.sort()

c = -1
ans = [0, 0]
for ai in a:
    for bi in b:
        t = ai+bi
        if t > 0 and t <= F and (E*ai//100) >= bi:
            tc = 100*bi/(ai+bi)
            if c < tc:
                c = tc
                ans = [t, bi]

print(*ans)
