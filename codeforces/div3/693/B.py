for t in range(int(input())):
    n = int(input())
    *a, = map(int, input().split())
    ans = "No"
    if n % 2 == 0:
        if sum(a) % 2 == 0:
            ans = "Yes"
    else:
        if a.count(1) >= 2 and sum(a) % 2 == 0:
            ans = "Yes"
    print(ans)
