N = int(input())
*a1, = map(int, input().split())
*a2, = map(int, input().split())
ans = 0
for i in range(N):
    t = sum(a1[:i+1])+sum(a2[i:])
    ans = max(t, ans)
print(ans)
