N, M = map(int, input().split())
ab = []
for i in range(M):
    a, b = map(int, input().split())
    ab.append((a, b))
ab.sort(key=lambda x: x[1])

ans, r = 0, 0
for a, b in ab:
    if a >= r:
        r = b
        ans += 1
print(ans)

'''
ab = []
for i in range(M):
    a, b = map(int, input().split())
    ab.append((a, b))
ab.sort()

l = [ab[0]]
for a, b in ab[1:]:
    la, lb = l[-1]
    if a < lb:
        l[-1] = (max(a, la), min(b, lb))
    else:
        l.append((a, b))

print(len(l))
'''
