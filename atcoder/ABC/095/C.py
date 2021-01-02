a, b, c, x, y = map(int, input().split())
ans = float('inf')
for i in range(max(x, y)+1):
    ab = i*2
    ans = min(ans, a*max(0, x-i)+b*max(0, y-i)+ab*c)
print(ans)
