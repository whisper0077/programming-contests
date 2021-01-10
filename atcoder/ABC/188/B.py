n = int(input())
*a, = map(int, input().split())
*b, = map(int, input().split())
ans = 0
for i in range(n):
    ans += a[i]*b[i]
if ans == 0:
    print("Yes")
else:
    print("No")
