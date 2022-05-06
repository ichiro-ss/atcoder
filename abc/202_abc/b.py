# input
s = str(input())

ans = ""
for c in s:
    if c == '0':
        ans = '0' + ans
    elif c == '1':
        ans = '1' + ans
    elif c == '6':
        ans = '9' + ans
    elif c == '8':
        ans = '8' + ans
    elif c == '9':
        ans = '6' + ans
print(ans)