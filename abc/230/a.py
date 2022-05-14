# input
n = int(input())

agc = "AGC"
if 0 < n < 10:
    print(agc + "00" + str(n))
elif n < 42:
    print(agc + "0" + str(n))
elif n < 100:
    print(agc + "0" + str(n + 1))
else:
    print(agc + str(n + 1))
    