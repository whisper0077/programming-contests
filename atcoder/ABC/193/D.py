from collections import defaultdict
K = int(input())
S = input()
T = input()
cards = [K]*10
cards[0] = 0

s = [int(v) for v in list(S[:-1])]
t = [int(v) for v in list(T[:-1])]
sh, th = [0]*11, [0]*11
for i in range(4):
    cards[s[i]] -= 1
    cards[t[i]] -= 1
    sh[s[i]] += 1
    th[t[i]] += 1

sumcard = sum(cards)
total = sumcard * (sumcard-1)
tk = 0
for a in range(1, 10):
    if cards[a] <= 0:
        continue
    aa = cards[a]
    cards[a] -= 1
    sh[a] += 1
    for b in range(1, 10):
        if cards[b] <= 0:
            continue
        bb = cards[b]
        cards[b] -= 1
        th[b] += 1

        ss = sum(i*10**sh[i] for i in range(1, 11))
        ts = sum(i*10**th[i] for i in range(1, 11))
        if ss > ts:
            #print(a, b, aa, bb, ss, ts)
            tk += aa*bb
        th[b] -= 1
        cards[b] += 1
    cards[a] += 1
    sh[a] -= 1

print(tk/total)
