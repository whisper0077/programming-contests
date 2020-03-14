h, w = map(int, input().split())
if w == 1 or h == 1:
    print(1)
else:
    ans = (h//2)*w
    if h % 2 == 1:
        ans += (w+1)//2
    print(ans)
