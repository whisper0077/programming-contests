import itertools

T = int(input())
for t in range(T):
    n, k = map(int, input().split())
    s = input().strip()
    a = [0]*n
    for i in range(n):
        if s[i] == "1":
            l, r = max(i-k, 0), (i+k+1)
            a[l] += 1
            if r < n:
                a[r] -= 1
    a = list(itertools.accumulate(a))
    ans = 0
    i = 0
    while i < n:
        if a[i] == 0:
            ans += 1
            i += k+1
        else:
            i += 1
    print(ans)
