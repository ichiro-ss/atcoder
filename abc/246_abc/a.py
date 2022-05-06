x = [0]*3; y = [0]*3
x[0], y[0] = [int(i) for i in input().split()]
x[1], y[1] = [int(i) for i in input().split()]
x[2], y[2] = [int(i) for i in input().split()]

if x[1] == x[2]:
    ans_x = x[0]
elif x[0] == x[1]:
    ans_x = x[2]
else:
    ans_x = x[1]

if y[1] == y[2]:
    ans_y = y[0]
elif y[0] == y[1]:
    ans_y = y[2]
else:
    ans_y = y[1]

print(ans_x, ans_y)