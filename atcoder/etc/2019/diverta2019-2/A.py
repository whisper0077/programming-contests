n, k = map(int, input().split())
l = [1]*k
n -= sum(l)
l[0] += n
print(max(l)-min(l))
