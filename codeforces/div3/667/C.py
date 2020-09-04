for t in range(int(input())):
    n, x, y = map(int, input().split())
    m = 0
    for i in range(1, y-x+1):
        if (y-x) % i == 0:
            a = (y-x)//i+1
            if a <= n:
                c = n-a
                while c > 0 and (x-i) > 0:
                    x -= i
                    c -= 1
                while c > 0:
                    y += i
                    c -= 1
                ans = [v for v in range(x, y+1, i)]
                print(*ans)
                break
