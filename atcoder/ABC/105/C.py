N = int(input())
ans = ""
while N != 0:
    if N % 2 == 0:
        ans = "0"+ans
        N //= -2
    else:
        ans = "1"+ans
        N = (N-1)//-2
print(ans if ans != "" else "0")
