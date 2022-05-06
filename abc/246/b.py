from cmath import sqrt


a, b = [int(i) for i in input().split()]

x = sqrt(a*a + b*b)
print(float(a/x), float(b/x))