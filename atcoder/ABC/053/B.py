S = input()
a, z = 0, 0
for i in range(len(S)):
    if S[i] == 'A':
        a = i
        break
for i in range(len(S)-1, -1, -1):
    if S[i] == 'Z':
        z = i
        break
print(z-a+1)
