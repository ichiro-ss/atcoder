# input
x, n = [int(i) for i in input().split()]
p = [int(i) for i in input().split()]

smaller, bigger = x, x
ans = []
while 1 <= smaller <= 100 or 1 <= bigger <= 100:
    if smaller not in p:
        ans.append(smaller)
    if bigger not in p:
        ans.append(bigger)
    if len(ans):
        break
    smaller -= 1
    bigger += 1

if len(ans) == 2 and ans[0] == ans[1]:
        print(ans[0])
else:
    print(ans[0])