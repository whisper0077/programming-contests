c = [list(map(int, input().split())) for _ in range(3)]
ans = "No"
for a1 in range(101):
    for a2 in range(101):
        for a3 in range(101):
            b1 = (c[0][0]-a1) == (c[1][0]-a2) and (c[0][0]-a1) == (c[2][0]-a3)
            b2 = (c[0][1]-a1) == (c[1][1]-a2) and (c[0][1]-a1) == (c[2][1]-a3)
            b3 = (c[0][2]-a1) == (c[1][2]-a2) and (c[0][2]-a1) == (c[2][2]-a3)
            if b1 and b2 and b3:
                ans = "Yes"
print(ans)
