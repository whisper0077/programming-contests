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
    cnt = 0
    for k in range(left, right):
        c += 1
        if l[i] <= r[j]:
            a[k] = l[i]
            i += 1
        else:
            a[k] = r[j]
            j += 1
            cnt += n1 - i
    return cnt


def mergeSort(a, left, right):
    cnt = 0
    if (left + 1) < right:
        mid = (left + right) // 2
        cnt += mergeSort(a, left, mid)
        cnt += mergeSort(a, mid, right)
        cnt += merge(a, left, mid, right)
    return cnt


n = int(input())
*s, = map(int, input().split())

print(mergeSort(s, 0, n))
