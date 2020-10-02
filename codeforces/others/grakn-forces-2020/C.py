ans = []
for t in range(int(input())):
    n, l = map(int, input().split())
    *a, = map(int, input().split())
    n += 2
    a = [0]+a+[l]
    ls = [0]*n
    rs = [0]*n
    for i in range(1, n):
        ls[i] = ls[i-1]+(a[i]-a[i-1])/i
    for i in range(n-2, -1, -1):
        rs[i] = rs[i+1]+(a[i+1]-a[i])/(n-1-i)

    for i in range(n-1):
        if ls[i] <= rs[i] and ls[i+1] > rs[i+1]:
            vx, vy = i+1, n-1-i
            tx, ty = ls[i], rs[i+1]
            m = a[i+1]-a[i]
            if tx > ty:
                m -= vy*(tx-ty)
            else:
                m -= vx*(ty-tx)
            dt = m/(vx+vy)
            ans.append(max(tx, ty)+dt)
            break

for a in ans:
    print(a)
