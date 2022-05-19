# input
d = int(input())
c = [int(_) for _ in input().split()]
s = [[int(_) for _ in input().split()] for _ in range(d)]

# greedy algorithm
num = 26
last = [0] * num

def decrease(d):
    dec_v = 0
    for i in range(num):
        dec_v += c[i] * ((d + 1) - last[i])
    return dec_v

v = 0
for i in range(d):
    max_t, max_v = 0, 0
    for t in range(num):
        tmp_v = v
        tmp = last[t]
        last[t] = i + 1
        tmp_v += s[i][t]
        tmp_v -= decrease(i)
        if max_v < tmp_v:
            max_t = t
            max_v = tmp_v
        last[t] = tmp
    last[max_t] = i + 1
    v = max_v
    print(max_t + 1)