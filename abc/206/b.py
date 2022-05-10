# input
n = int(input())

money = 0
for i in range(1, n+1):
    money += i
    if money >= n:
        print(i)
        break
