N = int(input())
*A, = map(int, input().split())
ans = 0
while True:
    ok = True
    for i in range(N):
        if A[i] % 2 != 0:
            ok = False
            break
        A[i] //= 2
    if not ok:
        break
    ans += 1
print(ans)
