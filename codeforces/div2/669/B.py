
for t in range(int(input())):
    n = int(input())
    *a, = map(int, input().split())
    a.sort(reverse=True)
    ans = [a[0]]
    a = a[1:]
    n -= 1
    last = ans[-1]
    for i in range(last, 0, -1):
        if last % i != 0:
            continue
        for j in range(n):
            if a[j] > 0 and a[j] % i == 0:
                ans.append(a[j])
                a[j] = -1
                last = i
    for i in range(n):
        if a[i] > 0:
            ans.append(a[i])
    print(*ans)
