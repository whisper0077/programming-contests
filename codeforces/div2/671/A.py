for t in range(int(input())):
    n = int(input())
    s = input()
    if n % 2 == 0:
        ans = 1
        for i in range(n):
            if i % 2 == 1 and int(s[i]) % 2 == 0:
                ans = 2
                break
        print(ans)
    else:
        ans = 2
        for i in range(n):
            if i % 2 == 0 and int(s[i]) % 2 == 1:
                ans = 1
                break
        print(ans)
