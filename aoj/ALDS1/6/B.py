'''
Partition(A, p, r)
1 x = A[r]
2 i = p-1
3 for j = p to r-1
4     do if A[j] <= x
5        then i = i+1
6            exchange A[i] and A[j] 
7 exchange A[i+1] and A[r]
8 return i+1
'''


def partition(a, p, r):
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1


n = int(input())
*s, = map(int, input().split())

c = partition(s, 0, n - 1)
for i in range(n):
    s[i] = f"[{s[i]}]" if i == c else s[i]
print(" ".join([str(v) for v in s]))
