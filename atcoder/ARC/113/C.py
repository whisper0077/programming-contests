from collections import defaultdict
S = input().strip()
c = defaultdict(int)
c[S[-1]] = 1
t = 1
ans = 0
for i in range(len(S)-2, 0, -1):
    if S[i] == S[i-1] and S[i] != S[i+1]:
        ans += t-c[S[i]]
        c = defaultdict(int)
        c[S[i]] = t
    c[S[i]] += 1
    t += 1
print(ans)
