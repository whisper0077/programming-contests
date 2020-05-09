N = int(input())
*a, = map(int, input().split())
a.sort()
print(a[-1]-a[0])
