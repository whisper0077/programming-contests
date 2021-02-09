N = int(input())
*a, = map(int, input().split())
ans = 0
for i in range(N):
    while a[i] % 2 == 0:
        ans += 1
        a[i] //= 2
print(ans)
