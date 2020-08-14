from collections import defaultdict
import itertools
for t in range(int(input())):
    n = int(input())
    a = [int(v) for v in list(input())]
    a = list(itertools.accumulate(a))
    c = defaultdict(int)

    ans = 0
    for i in range(n):
        ai = a[i]-i
        ans += c[ai]
        c[ai] += 1
        if ai == 1:
            ans += 1
    print(ans)

    '''
    ans = 0
    a = [0]+a
    for i in range(1, n+1):
        l, r = a[i-1]-i+1, a[i]-i
        c[l] += 1
        ans += c[r]
    print(ans)
    '''
