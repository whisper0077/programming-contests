N = int(input())
A = [int(input()) for _ in range(N)]
s = sorted(A)
s.reverse()
for i in range(N):
    if A[i] == s[0]:
        print(s[1])
    else:
        print(s[0])
