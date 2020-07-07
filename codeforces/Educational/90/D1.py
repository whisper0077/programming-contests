'''
D. Maximum Sum on Even Positions
ある数列Aがあり、Aの連続する部分列を1つ選んで反転させる（ある区間）
反転後に偶数番目の和が最大となるようにする
その時の和を求める

耳DPというので求めることができる

dp[i][0] := 反転を開始していない状態(左を選択していない)
dp[i][1] := 反転を開始したが、反転終了していない(右を選択していない)
dp[i][2] := 反転終了した状態
'''

for t in range(int(input())):
    n = int(input())
    *a, = map(int, input().split())

    dp = [[0]*3 for _ in range(n+2)]
    for i in range(n):
        # 反転を開始していない
        dp[i+1][0] = dp[i][0] + (a[i] if i % 2 == 0 else 0)

        # 反転開始したが、終了していない
        if i+1 < n:
            dp[i+2][1] = max(dp[i][0], dp[i][1]) + (a[i+1] if i % 2 == 0 else a[i])

        # 反転終了している
        dp[i+1][2] = max(dp[i][1], dp[i][2])+(a[i] if i % 2 == 0 else 0)

    print(max(dp[n]))
