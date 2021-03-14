N = int(input())
ans = 0
d = 999
while (N-d) > 0:
    ans += N-d
    d = d*1000+999
print(ans)
