import itertools
# input
n = int(input())
p = tuple([int(i) for i in input().split()])
q = tuple([int(i) for i in input().split()])

perms = list(itertools.permutations(range(1, n+1), n))
a, b = 0, 0
for i, v in enumerate(perms):
    if v == p:
        a = i
    if v == q:
        b = i
print(abs(a - b))