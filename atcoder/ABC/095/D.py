N, C = map(int, input().split())
x, v = [0]*(N+1), [0]*(N+1)
s = [0]*(N+1)
for i in range(1, N+1):
    x[i], v[i] = map(int, input().split())
    s[i] = s[i-1]+v[i]

ans = 0
ccw0, ccw1 = 0, 0
for i in range(N, -1, -1):
    # 時計回りに行って、逆時計回りにiまで取る
    ans = max(ans, s[i]-2*x[i]+ccw0)
    if i > 0:
        ccw0 = max(ccw0, s[N]-s[i-1]-(C-x[i]))

    # 逆時計回りに行って、時計回りにiまで取る
    ans = max(ans, s[i]-x[i]+ccw1)
    if i > 0:
        ccw1 = max(ccw1, s[N]-s[i-1]-2*(C-x[i]))

print(ans)
