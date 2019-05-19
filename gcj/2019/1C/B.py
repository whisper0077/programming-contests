import sys


def fprint(s):
    print(s)
    sys.stdout.flush()


def ferr(s):
    sys.stderr.write(str(s) + "\n")
    sys.stderr.flush()


T, F = map(int, input().split())
for t in range(T):
    l = [i * 5 + 1 for i in range(119)]
    ans = []
    rest = {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1}
    for m in [23, 5, 1, 0]:
        h = {'A': [], 'B': [], 'C': [], 'D': [], 'E': []}
        for v in l:
            fprint(v)
            a = input().strip()
            h[a].append(v + 1)
        for k, v in h.items():
            if k in rest:
                #ferr("k,v = ({},{})".format(k, len(v)))
                if len(v) == m:
                    #ferr("found {}".format(k))
                    l = v
                    ans.append(k)
                    del rest[k]
                    break
    ans = "".join(ans) + list(rest.keys())[0]
    #ferr(ans)
    fprint(ans)
    a = input().strip()
    if a == 'N':
        sys.exit(1)
