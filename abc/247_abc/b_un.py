# input
n = int(input())
s = []; t = []
for _ in range(n):
    a, b = [str(i) for i in input().split()]
    s.append(a); t.append(b)


for i in range(n):
    can_be_called = False
    for a in [s[i], t[i]]:
        a_ok = True
        for j in range(n):
            if i != j:
                if a == s[j] or a == t[j]:
                    a_ok = False
        if a_ok:
            can_be_called = True
    if not can_be_called:
        print("No")
        exit()
print("Yes")
