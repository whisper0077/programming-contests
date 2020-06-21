
N = int(input())
*A, = map(int, input().split())
cnt = [0]*(10**5+1)
s = 0
for i in range(N):
    cnt[A[i]] += 1
    s += A[i]

Q = int(input())
for i in range(Q):
    B, C = map(int, input().split())
    d = (C-B)*cnt[B]
    s += d
    cnt[C] += cnt[B]
    cnt[B] = 0
    print(s)
