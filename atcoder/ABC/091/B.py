from collections import defaultdict
N = int(input())
h = defaultdict(int)
h["0"] = 0
for i in range(N):
    s = input()
    h[s] += 1

M = int(input())
for i in range(M):
    s = input()
    h[s] -= 1

print(max(h.values()))
