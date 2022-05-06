# input
n, k = [int(i) for i in input().split()]

for i in range(k):
    if not n % 200:
        n //= 200
    else:
        n = int(str(n) + "200")
print(n)