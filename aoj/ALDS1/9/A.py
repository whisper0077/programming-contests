h = int(input())
t = input().split()
for i in range(h):
    ans = f"node {i+1}: key = {t[i]}, "
    p = (i+1)//2-1
    if p >= 0:
        ans += f"parent key = {t[min([p,h])]}, "
    l, r = (i+1)*2-1, (i+1)*2
    if l < h:
        ans += f"left key = {t[l]}, "
        if r < h:
            ans += f"right key = {t[r]}, "
    print(ans)
