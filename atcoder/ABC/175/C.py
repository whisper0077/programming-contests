X, K, D = map(int, input().split())
X = abs(X)
n = X//D
if K < n:
    print(X-K*D)
else:
    if (n-K) % 2 == 0:
        print(X-n*D)
    else:
        print(abs(X-(n+1)*D))
