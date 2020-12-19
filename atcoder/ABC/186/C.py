N = int(input())
ans = 0
for i in range(1, N+1):
    s = str(i)
    s += oct(i)
    if not "7" in s:
        ans += 1
print(ans)
