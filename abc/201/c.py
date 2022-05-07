import math

# input
s = str(input())

def aCb(x, y):
    return math.factorial(x) // (math.factorial(x - y) * math.factorial(y))

cnts = {"o":0, "?":0, "x":0}
for c in s:
    cnts[c] += 1

if cnts["o"] > 4 or (cnts["o"] + cnts["?"]) < 1:
    print(0)
    exit()

ans = 0
for i in range(cnts["?"] + 1):
    if i + cnts["o"] == 0 or i + cnts["o"] > 4:
        continue

    used = i + cnts["o"]
    if used == 1:
        ans += aCb(cnts["?"], i)
    elif used == 2:
        ans += (2 * 4 + aCb(4, 2)) * aCb(cnts["?"], i)
    elif used == 3:
        ans += 3 * 4 * 3 * aCb(cnts["?"], i)
    elif used == 4:
        ans += 4 * 3 * 2 * aCb(cnts["?"], i)
print(ans)