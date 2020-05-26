S = input()
n = len(S)-1
while n > 0:
    if n % 2 == 1:
        n -= 1
        continue
    m = n//2
    if S[:m] == S[m:+2*m]:
        break
    n -= 1

print(n)
