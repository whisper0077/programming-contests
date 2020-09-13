N = int(input())
d = [[], []]
for i in range(N):
    x, y = map(int, input().split())
    d[0].append(x-y)
    d[1].append(x+y)

ans = 0
for i in range(2):
    ans = max(ans, max(d[i])-min(d[i]))
print(ans)
