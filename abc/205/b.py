# input
n = int(input())
a = [int(_) for _ in input().split()]

values = set()
for v in a:
    if v not in values:
        values.add(v)
for i in range(n):
    if i + 1 not in values:
        print("No")
        exit()
print("Yes")