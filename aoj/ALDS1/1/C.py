n = int(input())
ans = 0

for _ in range(n):
    v = int(input())
    if v == 2:
        ans += 1
    elif v % 2 > 0:
        i = 3
        p = False
        while (i*i) <= v:
            if v % i == 0:
                p = True
                break
            i += 2
        if not p:
            ans += 1
print(ans)
