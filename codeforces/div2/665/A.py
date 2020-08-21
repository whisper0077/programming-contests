for t in range(int(input())):
    n, k = map(int, input().split())
    if n <= k:
        print(k-n)
    else:
        a = n-k
        print(a % 2)
