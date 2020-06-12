N = int(input())
*a, = map(int, input().split())
two, four, no = 0, 0, 0
for i in range(N):
    if a[i] % 4 == 0:
        four += 1
    elif a[i] % 2 == 0:
        two += 1
    else:
        no += 1

ok = four == no or (four+two) == N
ok = ok or ((four+no) == N and abs(four-no) <= 1)
if ok:
    print("Yes")
else:
    print("No")
