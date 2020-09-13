N = int(input())
c = 0
ans = "No"
for i in range(N):
    d1, d2, = map(int, input().split())
    if d1 == d2:
        c += 1
        if c >= 3:
            ans = "Yes"
    else:
        c = 0

print(ans)
