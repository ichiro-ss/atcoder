# input
n = int(input())

value = int(1.08 * n)
if value < 206:
    print("Yay!")
elif value > 206:
    print(":(")
else:
    print("so-so")
