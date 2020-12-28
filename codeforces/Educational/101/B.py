from itertools import accumulate

anss = []
for t in range(int(input())):
    n = int(input())
    *r, = map(int, input().split())
    m = int(input())
    *b, = map(int, input().split())

    ans = 0
    rs = [0]+list(accumulate(r))
    bs = [0]+list(accumulate(b))
    for i in range(n+1):
        for j in range(m+1):
            ans = max(ans, rs[i]+bs[j])

    anss.append(ans)

for a in anss:
    print(a)
