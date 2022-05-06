# input
n = int(input())
a = [int(i) for i in input().split()]

# use a dictionary
# this solution is quite good though
# can be better with a little flash
# figs = {}
# for i in a:
#     if i in figs:
#         figs[i] += 1
#     else:
#         figs[i] = 1

# ans = 0
# for fig1 in figs:
#     for fig2 in figs:
#         if (fig1 * fig2) in figs:
#             ans += figs[fig1] * figs[fig2] * figs[fig1 * fig2]
# print(ans)

# 
ans = 0
figs = [0] * int(2 * 1e5 + 1)
for val in a:
    figs[val] += 1

fin = 0
for i in range(len(figs) - 1, -1, -1):
    if figs[i]:
        fin = i
        break
figs = figs[:fin + 1]

for i in range(1, len(figs)):
    for j in range(1, fin // i + 1):
        if figs[i] and figs[j] and figs[i * j]:
            ans += figs[i] * figs[j] * figs[i * j]

print(ans)