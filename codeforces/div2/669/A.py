for t in range(int(input())):
    n = int(input())
    *a, = map(int, input().split())
    ans = []
    if a.count(0) >= a.count(1):
        ans = [0]*(n//2)
    else:
        m = n//2+(n//2) % 2
        ans = [1]*m
    print(len(ans))
    print(*ans)
