import sys
h = 0
a = [-2**63]*2000001


def parent(i):
    return i//2


def left(i):
    return i*2


def right(i):
    return i*2+1


def maxHeapify(i):
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
        maxHeapify(mi)


def insert(k):
    global h
    h += 1
    increaseHeap(h, k)


def increaseHeap(i, k):
    a[i] = k
    while i > 1 and a[parent(i)] < a[i]:
        a[parent(i)], a[i] = a[i], a[parent(i)]
        i = parent(i)


def extract():
    global h
    m = a[1]
    a[1] = a[h]
    h -= 1
    maxHeapify(1)
    return m


for n in sys.stdin.read().splitlines():
    if n == "end":
        break
    if n == "extract":
        print(extract())
    else:
        v = n.split()[1]
        insert(int(v))
