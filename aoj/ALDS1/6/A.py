'''
Counting-Sort(A, B, k)
1    for i = 0 to k
2        do C[i] = 0
3    for j = 1 to length[A]
4        do C[A[j]] = C[A[j]]+1
5    /* C[i] now contains the number of elements equal to i */
6    for i = 1 to k
7    do C[i] = C[i] + C[i-1]
8    /* C[i] now contains the number of elements less than or equal to i */
9    for j = length[A] downto 1
10       do B[C[A[j]]] = A[j]
11          C[A[j]] = C[A[j]]-1
'''
k = 10000
c = [0] * (k + 1)


def countingSort(a, b):
    global k
    n = len(a) - 1
    for i in range(k + 1):
        c[i] = 0
    for j in range(n):
        c[a[j + 1]] += 1

    #print(c)

    for i in range(1, k + 1):
        c[i] = c[i] + c[i - 1]

    #print(c)
    for j in range(n):
        #print(a[j], c[a[j]])
        b[c[a[j + 1]]] = a[j + 1]
        c[a[j + 1]] -= 1


n = int(input())
*a, = map(int, input().split())
a.insert(0, 0)
b = [0] * (n + 1)

countingSort(a, b)
b.pop(0)
print(" ".join([str(v) for v in b]))