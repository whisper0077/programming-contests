from collections import defaultdict

N, K = map(int, input().split())
s = input()
ans = 0

for i in range(N - K + 1):
    for j in range(i + K - 1, N):
        t = len(set(s[i:j + 1]))
        if t == K:
            ans += 1
        elif t > K:
            break
print(ans)