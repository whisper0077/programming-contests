N = int(input())
S = input().strip()
ans = 0
for i in range(1, N-1):
    l, r = set(), set()
    for j in range(0, i):
        l.add(S[j])
    for j in range(i, N):
        r.add(S[j])
    ans = max(ans, len(l & r))

print(ans)
