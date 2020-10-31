N, K = map(int, input().split())
K = abs(K)
ans = 0

for ab in range(2, 2*N+1):
    cd = ab-K
    if cd >= 2:
        # a+b=ab
        mab = min(ab-1, 2*N-ab+1)
        mcd = min(cd-1, 2*N-cd+1)
        ans += mab*mcd
print(ans)
