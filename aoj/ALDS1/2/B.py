'''
SelectionSort(A)
1 for i = 0 to A.length-1
2     mini = i
3     for j = i to A.length-1
4         if A[j] < A[mini]
5             mini = j
6     swap A[i] and A[mini]
'''

n = int(input())
*v, = map(int, input().split())
c = 0
for i in range(n):
    mi = i
    for j in range(i, n):
        if v[j] < v[mi]:
            mi = j
    if mi != i:
        c += 1
    v[i], v[mi] = v[mi], v[i]


print(" ".join([str(_v) for _v in v]))
print(c)
