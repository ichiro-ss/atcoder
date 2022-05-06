# input
a, b, c, d, e, f, x = [int(i) for i in input().split()]

full_t = a + c
full_a = d + f

dis_t = a * (x // full_t) * b
dis_a = d * (x // full_a) * e

dis_t += min(x % full_t, a) * b
dis_a += min(x % full_a, d) * e

if dis_t < dis_a:
    print("Aoki")
elif dis_t > dis_a:
    print("Takahashi")
else:
    print("Draw")