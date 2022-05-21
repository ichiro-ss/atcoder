# input
n, k = [int(_) for _ in input().split()]
a = [int(_) for _ in input().split()]
b = [int(_) - 1 for _ in input().split()]

food = []
max_v = max(a)
for i in range(n):
    if a[i] == max_v:
        food.append(i)

for i in range(k):
    for j in food:
        if j == b[i]:
            print("Yes")
            exit()
print("No")