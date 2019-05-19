'''
Merge(A, left, mid, right)
  n1 = mid - left;
  n2 = right - mid;
  create array L[0...n1], R[0...n2]
  for i = 0 to n1-1
    do L[i] = A[left + i]
  for i = 0 to n2-1
    do R[i] = A[mid + i]
  L[n1] = SENTINEL
  R[n2] = SENTINEL
  i = 0;
  j = 0;
  for k = left to right-1
    if L[i] <= R[j]
      then A[k] = L[i]
           i = i + 1
      else A[k] = R[j]
           j = j + 1

Merge-Sort(A, left, right){
  if left+1 < right
    then mid = (left + right)/2;
         call Merge-Sort(A, left, mid)
         call Merge-Sort(A, mid, right)
         call Merge(A, left, mid, right)
'''
import math
c = 0
l = [0] * 500000
r = [0] * 500000


def merge(a, left, mid, right):
    global c
    n1 = mid - left
    n2 = right - mid
    for i in range(n1):
        l[i] = a[left + i]
    for i in range(n2):
        r[i] = a[mid + i]
    l[n1] = math.inf
    r[n2] = math.inf
    i, j = 0, 0
    for k in range(left, right):
        c += 1
        if l[i] <= r[j]:
            a[k] = l[i]
            i += 1
        else:
            a[k] = r[j]
            j += 1


def mergeSort(a, left, right):
    if (left + 1) < right:
        mid = (left + right) // 2
        mergeSort(a, left, mid)
        mergeSort(a, mid, right)
        merge(a, left, mid, right)


n = int(input())
*s, = map(int, input().split())

mergeSort(s, 0, n)

print(" ".join([str(v) for v in s]))
print(c)