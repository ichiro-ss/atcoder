# input
D = int(input())
c = [int(_) for _ in input().split()]
s = [[int(_) for _ in input().split()] for _ in range(D)]
contests = [int(input()) - 1 for _ in range(D)]
m = int(input())

num = 26
last = [[0 for _ in range(D)] for _ in range(num)]

# def decrease(day):
#     dec_v = 0
#     for i in range(num):
#         dec_v += c[i] * ((day + 1) - last[i][day])
#     return dec_v

def score():
    res = 0
    held = [False for _ in range(num)]
    for i in range(D):
        held[contests[i]] = True
        interval = (last[contests[i]][i] - last[contests[i]][i-1] + 1) if i > 0 else 1
        dec = c[contests[i]] * interval * (interval - 1) // 2
        res += s[i][contests[i]]
        res -= dec
        # res += s[i][contests[i]] - decrease(i)
    for i in range(num):
        if not held[i]:
            dec = c[i] * D * (D + 1) // 2
            res -= dec
    return res

# change the contest
def change_to(day, a):
    global last, contests
    pr_con = contests[day]
    contests[day] = a
    # print(contests)
    for i in range(day, D):
        if last[pr_con][i] == day + 1:
            if i == 0:
                last[pr_con][i] = 0
            else:
                last[pr_con][i] = last[pr_con][i-1]
        else:
            break
    for i in range(day, D):
        if last[a][i] < day + 1:
            last[a][i] = day + 1
        else:
            break

for i in range(D):
    day = i
    while day < D:
        last[contests[i]][day] = i + 1
        day += 1
        if day >= D or contests[day] == contests[i]:
            break

for i in range(m):
    d, q = [int(_) - 1 for _ in input().split()]
    change_to(d, q)
    print(score())
