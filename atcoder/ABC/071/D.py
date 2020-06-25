MOD = 1000000007
N = int(input())
s1 = input().strip()
s2 = input().strip()
ans = 1
i = 0
pi = -1
while i < N:
    if s1[i] != s2[i]:
        if i == 0:
            ans *= 6
        else:
            if s1[pi] != s2[pi]:
                ans *= 3
            else:
                ans *= 2
        pi = i
        i += 2
    else:
        if i == 0:
            ans *= 3
        else:
            if s1[pi] != s2[pi]:
                ans *= 1
            else:
                ans *= 2
        pi = i
        i += 1
    ans = ans % MOD

print(ans)
