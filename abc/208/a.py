# input
a, b = [int(_) for _ in input().split()]

if a <= b <= 6 * a:
    print("Yes")
else:
    print("No")