N, M = map(int, input().split())
if M != 0 and (M < 0 or M > N-2):
    print(-1)
else:
    ans = []
    if M == 0:
        for i in range(1, N+1):
            ans.append([i*2, i*2+1])
    else:
        for i in range(M+1):
            ans.append([i*2, i*2+1])
        ans.append([-1, (M+1)*2])
        for i in range(N-M-2):
            j = M+2+i
            ans.append([j*2, j*2+1])

    for i in range(N):
        l, r = ans[i]
        print(l+2, r+2)
