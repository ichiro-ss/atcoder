# input
x, y = [int(_) for _ in input().split()]
if x == y:
    print(x)
elif x + y == 1:
    print(2)
elif x + y == 2 and (x == 0 or y == 0):
    print(1)
else:
    print(0)