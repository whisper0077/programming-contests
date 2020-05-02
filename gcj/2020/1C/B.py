T = int(input())
for t in range(T):
    U = int(input())
    h = {}
    for i in range(10**4):
        q, r = input().split()
        for j in range(len(r)):
            ri = r[j]
            if not ri in h:
                h[ri] = 0
            if j == 0:
                h[ri] += 1
    a = []
    for k, v in h.items():
        if v == 0:
            a.append([-10**5, k])
        else:
            a.append([-v, k])
    a.sort()
    print("Case #{}: {}".format(t+1, "".join([k for v, k in a])))
