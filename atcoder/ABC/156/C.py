N = int(input())
*X, = map(int, input().split())
ans = 10**20
for i in range(100):
    s = sum([(x-i)*(x-i) for x in X])
    if s < ans:
        ans = s
print(ans)
