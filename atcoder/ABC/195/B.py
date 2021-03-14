A, B, W = map(int, input().split())
W *= 1000
l, r = 10**10, 0
for i in range(1, 10**6+1):
    a, b = A*i, B*i
    if a <= W and W <= b:
        l = min(i, l)
        r = max(i, r)
if l > r:
    print("UNSATISFIABLE")
else:
    print(l, r)
