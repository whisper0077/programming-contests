a, b, x = map(int, input().split())
ans = (b+x)//x
if a > 0:
    ans -= (a+x-1)//x
print(ans)
