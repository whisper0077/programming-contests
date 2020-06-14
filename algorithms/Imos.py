from itertools import accumulate

if __name__ == "__main__":
    '''
    N個のランプがある
    Ai(0<=i<N)はランプの強さで、自身の左右Aiまでを照らす
    ランプの強さは回数ごとに、照らされた個数に上書きされる
    K回過ぎたときのランプの状態を求める

    Imos法
    重複する区間がいくつあるかを調べる
    区間の開始、終了にそれぞれ+1/-1して累積和を取る
    '''
    N, K = 7, 3
    A = [0, 0, 0, 1, 0, 0, 0]
    for i in range(K):
        a = [0]*N
        for j in range(N):
            l, r = max(j-A[j], 0), (j+A[j]+1)
            a[l] += 1
            if r < N:
                a[r] -= 1
        A = list(accumulate(a))

    print(*A)
