from collections import Counter
N = int(input())
*A, = map(int, input().split())
c = Counter(A)
ac = [(k, v) for k, v in c.items()]
ac.sort()
ac.reverse()

rest = 4
ans = 0
for k, v in ac:
    if v >= 4 and rest == 4:
        ans = k*k
        break
    elif v >= 2:
        rest -= 2
        if ans == 0:
            ans = -k
        else:
            ans *= -k
            break
print(max(ans, 0))
