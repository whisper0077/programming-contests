T = int(input())
for t in range(T):
    n = int(input())
    *a, = map(int, input().split())
    even, odd = 0, 0
    for i in range(n):
        if i % 2 != a[i] % 2:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1

    if even == odd:
        print(even)
    else:
        print(-1)
