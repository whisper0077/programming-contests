a = []
for i in range(3):
    a.append(list(map(int, input().split())))

N = int(input())
ans = "No"
for i in range(N):
    b = int(input())
    for y in range(3):
        for x in range(3):
            if a[y][x] == b:
                a[y][x] = 0

    for j in range(3):
        if sum(a[j]) == 0:
            ans = "Yes"
            break
    for j in range(3):
        s = 0
        for k in range(3):
            s += a[k][j]
        if s == 0:
            ans = "Yes"
            break
    if (a[0][0]+a[1][1]+a[2][2]) == 0 or (a[0][2]+a[1][1]+a[2][0]) == 0:
        ans = "Yes"
        break
    if ans == "Yes":
        break
print(ans)
