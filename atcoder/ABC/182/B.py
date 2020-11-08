N = int(input())
*A, = map(int, input().split())
ans, num = 0, 0
for i in range(2, max(A)+1):
    c = 0
    for a in A:
        if a % i == 0:
            c += 1
    if c > num:
        ans = i
        num = c
print(ans)
