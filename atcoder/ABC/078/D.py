N, Z, W = map(int, input().split())
*a, = map(int, input().split())
if N == 1:
    print(abs(a[0]-W))
else:
    print(max(abs(a[-1]-W), abs(a[-2]-a[-1])))
