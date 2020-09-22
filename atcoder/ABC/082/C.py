from collections import defaultdict
N = int(input())
*a, = map(int, input().split())
b = defaultdict(int)
for i in range(N):
    b[a[i]] += 1
ans = 0
for i, v in b.items():
    if i > b[i]:
        ans += b[i]
    elif i < b[i]:
        ans += b[i]-i
print(ans)
