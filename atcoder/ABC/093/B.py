A, B, K = map(int, input().split())
a = []
for i in range(A, min(A+K, B+1)):
    if not i in a:
        a.append(i)
for i in range(B, max(B-K, A-1), -1):
    if not i in a:
        a.append(i)
a.sort()
for i in a:
    print(i)
