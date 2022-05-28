# input
a, b, c = [int(_) for _ in input().split()]
if a <= b <= c:
    print("Yes")
elif c <= b <= a:
    print("Yes")
else:
    print("No")