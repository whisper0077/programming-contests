MOD = 10**9+7
for t in range(int(input())):
    N, A, B = map(int, input().split())
    if A < B:
        A, B = B, A

    ans = pow(N-A+1, 2, MOD) * pow(N-B+1, 2, MOD)

    # 重なる数xを求めて、ansから引く
    d = N-A-B
    if d >= 0:
        # まず重ならない数を求める
        # 空白マス+2から、2つ選ぶ場合の数
        x = (d+2)*(d+1)//2
        x %= MOD
        # 赤と青は対称性がある
        x = x*2
        x %= MOD
        # 一次元を考えたときに、A,Bの置き方総数から重ならない数を引いて
        # 重なる数を求める
        x = (N-A+1)*(N-B+1)-x
        x %= MOD
        # 2次元にする
        x = x*x
        x %= MOD
        ans = (ans-x) % MOD
    else:
        ans = 0

    print(ans)
