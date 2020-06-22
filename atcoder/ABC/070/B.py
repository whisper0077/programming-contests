A, B, C, D = map(int, input().split())
ans = min(B, D)-max(A, C)
print(max(ans, 0))
