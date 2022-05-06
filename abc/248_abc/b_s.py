a, b, k = [int(i) for i in input().split()]

i = 0
while a < b:
    i += 1
    a *= k
print(i)