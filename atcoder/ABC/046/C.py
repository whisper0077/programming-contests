N = int(input())
T, A = 1, 1
for i in range(N):
    t, a = map(int, input().split())
    # それぞれ一番近い倍数をもとめる
    tt = (T + t - 1) // t
    at = (A + a - 1) // a
    # 大きい方で掛ける
    mt = max([tt, at])
    T = t * mt
    A = a * mt
print(T + A)
