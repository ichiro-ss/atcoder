# input
a, b, c = [int(_) for _ in input().split()]

ans = ""
if c % 2:
    if a < 0 and b < 0:
        if a < b:
            ans = ">"
        elif a > b:
            ans = "<"
        else:
            ans = "="
    else:
        if a < b:
            ans = "<"
        elif a > b:
            ans = ">"
        else:
            ans = "="
else:
    if abs(a) < abs(b):
        ans = "<"
    elif abs(a) > abs(b):
        ans = ">"
    else:
        ans = "="
print(ans)