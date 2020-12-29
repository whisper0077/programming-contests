for t in range(int(input())):
    n, k = map(int, input().split())
    *h, = map(int, input().split())
    bottom, top = h[0], h[0]
    ans = "Yes"
    for i in range(1, n):
        bottom = max(bottom+1-k, h[i])
        top = min(h[i]+k-1, top+k-1)
        if bottom > top:
            ans = "No"
            break

    if ans == "Yes":
        if not (bottom <= h[-1] and h[-1] <= top):
            ans = "No"

    print(ans)
