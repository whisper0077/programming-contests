import itertools

N, M, Q = map(int, input().split())
abcd = []
for i in range(Q):
    *v, = map(int, input().split())
    abcd.append(v)

ans = 0
c = [i for i in range(1, M+1)]
for A in itertools.combinations_with_replacement(c, N):
    ta = 0
    for a, b, c, d in abcd:
        if (A[b-1]-A[a-1]) == c:
            ta += d
    if ans < ta:
        ans = ta

print(ans)
