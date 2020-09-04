for t in range(int(input())):
    a, b = map(int, input().split())
    c = abs(a-b)
    ans = c//10
    ans += 0 if c % 10 == 0 else 1
    print(ans)
