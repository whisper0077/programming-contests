N, M = map(int, input().split())
if M > 0:
    *A, = map(int, input().split())
    A.sort()
    A = [0]+A+[N+1]
    b = []
    for i in range(1, M+2):
        e = A[i]-A[i-1]-1
        if e > 0:
            b.append(e)

    b.sort()

    ans = 0
    if len(b) > 0:
        k = b[0]
        for i in range(len(b)):
            ans += (b[i]+k-1)//k
    print(ans)
else:
    print(1)
