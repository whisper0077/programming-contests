N, M = map(int, input().split())
t = 2**M
ans = (1900*M+100*(N-M))*t
print(ans)
