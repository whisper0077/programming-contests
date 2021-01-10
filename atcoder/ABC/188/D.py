import sys
input = sys.stdin.readline

N, C = map(int, input().split())
l = []
for i in range(N):
    a, b, c = map(int, input().split())
    l.append([a, c])
    l.append([b+1, -c])
l.sort()

ans = 0
t = 0
for i in range(len(l)-1):
    a, v = l[i]
    t += v
    b, v1 = l[i+1]
    d = b-a
    ans += min(C*d, t*d)

print(ans)
