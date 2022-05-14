# input
s = str(input())

if len(s) <= 2:
    if len(s) < 2:
        print("Yes")
    elif s == "oo":
        print("No")
    else:
        print("Yes")
    exit()
else:
    pre2, pre1 = s[0], s[1]
    if pre2 == "o" and pre1 == "o":
        print("No")
        exit()
    for i in range(2, len(s)):
        if s[i] == "x":
            if pre2 == "x" and pre1 == "x":
                print("No")
                exit()
        if s[i] == "o":
            if pre1 == "o" or pre2 == "o":
                print("No")
                exit()
        pre2 = pre1
        pre1 = s[i]
print("Yes")