s = input().strip()
yy, mm = int(s[:2]), int(s[2:])

yymm = False
mmyy = False
if 1 <= mm and mm <= 12:
    yymm = True
if 1 <= yy and yy <= 12:
    mmyy = True

if yymm and mmyy:
    print("AMBIGUOUS")
elif yymm:
    print("YYMM")
elif mmyy:
    print("MMYY")
else:
    print("NA")