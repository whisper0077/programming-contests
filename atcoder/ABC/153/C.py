N, K = map(int, input().split())
*H, = map(int, input().split())
H.sort(key=lambda x: -x)
H = H[K:]
print(sum(H))
