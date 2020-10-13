from collections import defaultdict
N, S = input().split()
N = int(N)

ans = 0
for i in range(N):
    c = defaultdict(int)
    for j in range(i, N):
        c[S[j]] += 1
        if (j-i) > 0:
            if c['A'] == c['T'] and c['G'] == c['C']:
                ans += 1
print(ans)
