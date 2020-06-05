L, R = map(int, input().split())
lr = R-L
if lr >= 2019:
    print(0)
else:
    ans = 2018
    for i in range(L, R+1):
        for j in range(i+1, R+1):
            t = i*j % 2019
            if t < ans:
                ans = t
    print(ans)
