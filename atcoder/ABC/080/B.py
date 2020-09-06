N = input().strip()
n = int(N)
fn = 0
for s in N:
    fn += int(s)

if n % fn == 0:
    print("Yes")
else:
    print("No")
