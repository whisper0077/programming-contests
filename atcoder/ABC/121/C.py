from collections import deque
N, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N)]
ab.sort()

ab = deque(ab)

ans = 0
m = 0
while m < M:
    a, b = ab.popleft()
    tm = min([b, M - m])
    ans += tm * a
    m += tm
print(ans)