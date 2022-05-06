# input
x = [int(i) for i in input().split()]

for i in range(5):
    if x[i] == 0:
        print(i + 1)