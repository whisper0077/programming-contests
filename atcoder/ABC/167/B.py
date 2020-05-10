A, B, C, K = map(int, input().split())
ans = 0
ans += min(K, A)
K = K-A-B
ans += min(max(K, 0), C)*-1
print(ans)
