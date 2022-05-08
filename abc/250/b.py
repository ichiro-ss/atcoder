# input
n, a, b = [int(_) for _ in input().split()]

col = ""
op = ""
cnt = 0
for i in range(n * b):
    if i // b % 2:
        col = col + "#"
        op = op + "."
    else:
        col = col + "."
        op = op + "#"
for i in range(n * a):
    if i // a % 2:
        print(op)
    else:
        print(col)