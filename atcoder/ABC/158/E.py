from fractions import gcd

N, P = map(int, input().split())
S = input().strip()

if gcd(10, P) > 1:
    ans = 0
    for i in range(len(S)):
        s = int(S[i])
        if s % P == 0:
            ans += (i+1)
    print(ans)
else:
    p = [0]*P
    ans = 0
    s = 0
    for i in range(len(S)-1, -1, -1):
        s = (s + int(S[i])*pow(10, N-1-i, P)) % P
        if s == 0:
            p[s] += 1
            ans += p[s]
        else:
            ans += p[s]
            p[s] += 1

    print(ans)
