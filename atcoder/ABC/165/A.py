K = int(input())
A, B = map(int, input().split())

ans = "NG"
a = A//K * K
while a <= B:
    if a >= A:
        ans = "OK"
    a += K
print(ans)
