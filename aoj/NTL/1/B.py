M, N = map(int, input().split())
div = 1000000007


def pos(x, n):
    if n == 0:
        return 1
    r = pos(x*x % div, n//2) % div
    if n % 2 == 1:
        r = (r*x) % div
    return r


print(pos(M, N))

'''
競技プログラミングでよくある
M=1000000007
で割る、というやつ

足し算 -> 加算ごとに%M
引き算 -> 引かれる値にMを足してから引き算して%M
掛け算 -> 乗算ごとに%M
    aをMで割った余りと商をar,aq
    bをMで割った余りと商をbr,bq
    a * b = (aq * M + ar) * (bq * M + br)
          = aq * bq * M2 + ar * bq * M + aq * br * M + ar * br
          = (...) * M + ar * br
'''
