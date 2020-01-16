N, K = map(int, input().split())
*a, = map(int, input().split())

# dp[i]=石の数がi個の場合の手番の人の勝ち負け
dp = [False]*(K+1)

for i in range(1, K+1):
    for j in range(N):
        # 遷移先にFalseがあればTrueにする
        # TrueになったらFalseにはならないため、orで入れる
        if i >= a[j]:
            dp[i] |= not dp[i-a[j]]

print("First" if dp[K] else "Second")
