import itertools
N = int(input())
*L, = map(int, input().split())
ans = 0
for l in itertools.combinations(L, 3):
    l = list(l)
    l.sort()
    if l[0] != l[1] and l[1] != l[2] and l[0] != l[2]:
        if l[2] < (l[0]+l[1]):
            ans += 1
print(ans)
