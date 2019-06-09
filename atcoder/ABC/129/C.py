n, m = map(int, input().split())
s = [0] * (n + 2)
s[0] = 1
s[1] = 1
for i in range(m):
    a = int(input())
    s[a] = -1

for i in range(2, n + 1):
    if s[i] < 0:
        continue
    if s[i - 2] > 0:
        s[i] += s[i - 2]
    if s[i - 1] > 0:
        s[i] += s[i - 1]
print(s[n] % 1000000007)
