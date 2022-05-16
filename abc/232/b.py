# input
s = str(input())
t = str(input())
def difference(a, b):
    if ord(a) <= ord(b):
        return ord(b) - ord(a)
    else:
        return 26 - (ord(a) - ord(b))

dif = difference(s[0], t[0])
ans = "Yes"
for i in range(1, len(s)):
    if dif != difference(s[i], t[i]):
        ans = "No"
print(ans)