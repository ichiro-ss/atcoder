import math
# input
n, a, b = [int(_) for _ in input().split()]

all_sigma = n * (1 + n) // 2

n_a = n // a
a_sigma = (n_a) * (2 * a + (n_a - 1) * a) // 2

n_b = n // b
b_sigma = (n_b) * (2 * b + (n_b - 1) * b) // 2

l_ab = a * b // math.gcd(a, b)
n_ab = n // l_ab
ab_sigma = (n_ab) * (2 * l_ab + (n_ab - 1) * l_ab) // 2

print(all_sigma - a_sigma - b_sigma + ab_sigma)