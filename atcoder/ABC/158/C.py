import math
A, B = map(int, input().split())
ans = -1
for i in range(1, 10001):
    a = i*0.08
    b = i*0.1
    if math.floor(a) == A and math.floor(b) == B:
        ans = i
        break
print(ans)
