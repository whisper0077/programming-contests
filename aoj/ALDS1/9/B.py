h = int(input())
n = [0]*(h+1)
n[1:] = [int(v) for v in input().split()]


def left(i):
    return i*2


def right(i):
    return i*2+1


def maxHeapify(a, i):
    '''
    i節点を可能な限り下降させる
    '''
    l, r = left(i), right(i)
    mi = i
    if l <= h and a[l] > a[i]:
        mi = l
    if r <= h and a[r] > a[mi]:
        mi = r

    if i != mi:
        a[i], a[mi] = a[mi], a[i]
        maxHeapify(a, mi)


def buildMaxHeap(a):
    i = h//2
    while i > 0:
        maxHeapify(a, i)
        i -= 1


buildMaxHeap(n)
print(" "+" ".join([str(v) for v in n[1:]]))
