import bisect
n = int(input())
a = [int(input()) for _ in range(n)]
l = [0]*n

'''
最長増加部分列問題
'''
li = 0
l[0] = a[0]
for i in range(1, n):
    if a[i] > l[li]:
        li += 1
        l[li] = a[i]
    else:
        j = bisect.bisect_left(l[:li], a[i])
        l[j] = a[i]
print(li+1)
