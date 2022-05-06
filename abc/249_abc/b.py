# input
s = str(input())

cnt_u, cnt_l = 0, 0

saw = set()
for c in s:
    if c not in saw:
        saw.add(c)
    else:
        print("No")
        exit()
    if cnt_l == 0 and c.islower():
        cnt_l += 1
    if cnt_u == 0 and c.isupper():
        cnt_u += 1
if cnt_l and cnt_u:
    print("Yes")
else:
    print("No")