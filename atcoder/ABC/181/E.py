import bisect
from itertools import accumulate

N, M = map(int, input().split())
*H, = map(int, input().split())
H.sort()

*W, = map(int, input().split())

if N == 1:
    ans = float('inf')
    for w in W:
        ans = min(ans, abs(H[0]-w))
    print(ans)
else:
    even = []
    odd = []
    for i in range(N-1):
        if i % 2 == 0:
            even.append(abs(H[i]-H[i+1]))
        else:
            odd.append(abs(H[i]-H[i+1]))

    even = list(accumulate(even))
    odd = list(accumulate(odd))

    ans = float('inf')
    for w in W:
        wi = bisect.bisect_left(H, w)
        c = 0
        if wi % 2 == 0:
            if wi == 0:
                c = abs(H[0]-w)+odd[-1]
            else:
                c = even[wi//2-1]
                c += abs(H[wi]-w)
                c += odd[-1]-odd[wi//2-1]
        else:
            if wi == 1:
                c = odd[-1]+abs(H[0]-w)
            else:
                c = even[wi//2-1]
                c += abs(H[wi-1]-w)
                c += odd[-1]-odd[wi//2-1]
        ans = min(ans, c)
    print(ans)
