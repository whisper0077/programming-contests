n = int(input())
ab = []

for i in range(n):
    ai, bi = map(int, input().split())
    ab.append([2*ai+bi, ai, bi])
ab.sort(reverse=True)

ac, bc = [0], [0]
for i in range(n):
    ac.append(ac[-1]+ab[i][1])
    bc.append(bc[-1]+ab[i][2])

for i in range(n+1):
    va = ac[-1]-ac[i]
    vb = ac[i]+bc[i]
    if va < vb:
        print(i)
        break
