N = int(input())
d = [0]*(10**6+1)
for i in range(1, 10**6+1):
    d[i] = d[i-1]+i

ans = 0
for i in range(N):
    a, b = map(int, input().split())
    ans += d[b]-d[a-1]
print(ans)
