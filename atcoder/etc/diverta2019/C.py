from collections import defaultdict

N = int(input())
s = [input().strip() for _ in range(N)]

h = defaultdict(int)
ans = 0
for si in s:
    ans += si.count('AB')
    if si[0] == 'B' and si[-1] == 'A':
        h['BA'] += 1
    elif si[0] == 'B':
        h['B'] += 1
    elif si[-1] == 'A':
        h['A'] += 1

if h['BA'] > 0:
    ans += h['BA']-1
    if h['B'] > 0:
        ans += 1
        h['B'] -= 1
    if h['A'] > 0:
        ans += 1
        h['A'] -= 1

ans += min(h['B'], h['A'])

print(ans)
