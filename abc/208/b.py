# input
p = int(input())

yen = 1
cnt = 0
for i in range(1, 10):
    r = int(p % (yen * (i + 1)))
    cnt += int(r / yen)
    yen *= (i + 1)
    p -= r
cnt += int(p / yen)
print(cnt)