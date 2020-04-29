N, A, B = map(int, input().split())
h = [int(input()) for _ in range(N)]
h.sort()

ans = 0
l, r = 1, max(h)//B+1
while l < r:
    m = (l+r)//2
    c = m
    for i in range(N):
        t = h[i]-m*B
        if t > 0:
            c -= (t+A-B-1)//(A-B)
            if c < 0:
                break

    if c >= 0:
        r = m
    else:
        l = m+1

print(l)
