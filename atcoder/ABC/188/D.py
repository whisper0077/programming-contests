import sys
input = sys.stdin.readline

N, C = map(int, input().split())
l = []
last = 0
for i in range(N):
    a, b, c = map(int, input().split())
    l.append([a, c])
    l.append([b+1, -c])
    last = max(last, b+1)
l.sort()

ans = 0
t = 0
for i in range(len(l)-1):
    a, v = l[i]
    if a >= last:
        break
    t += v
    b, v1 = l[i+1]
    d = b-a
    ans += min(C*d, t*d)


print(ans)
