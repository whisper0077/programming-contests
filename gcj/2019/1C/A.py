junken = {'R': 'P', 'S': 'R', 'P': 'S'}
T = int(input())
for t in range(T):
    A = int(input())
    p = {}
    for i in range(A):
        p[i] = input().strip()

    ans = ''
    i = 0
    while len(p) > 0:
        h = {}
        for k, v in p.items():
            g = v[i % (len(v))]
            if g not in h:
                h[g] = []
            h[g].append(k)
        if len(h) == 3:
            ans = 'IMPOSSIBLE'
            break
        else:
            ck = None
            if len(h) == 1:
                ck = list(h.keys())[0]
            else:
                if 'R' not in h:
                    ck = 'P'
                elif 'S' not in h:
                    ck = 'R'
                else:
                    ck = 'S'
            ans += junken[ck]
            for j in h[ck]:
                del p[j]
            i += 1
    print("Case #{}: {}".format(t + 1, ans))
