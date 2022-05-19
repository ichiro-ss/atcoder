# input
d = int(input())
c = [int(_) for _ in input().split()]
s = [[int(_) for _ in input().split()] for _ in range(d)]
t = [0] * d
for i in range(d):
    t[i] = int(input())

num = 26
last = [0] * num

def decrease(d):
    dec_v = 0
    for i in range(num):
        dec_v += c[i] * ((d + 1) - last[i])
    return dec_v

v = 0
for i in range(d):
    last[t[i] - 1] = i + 1
    v += s[i][t[i] - 1]
    v -= decrease(i)
    print(v)