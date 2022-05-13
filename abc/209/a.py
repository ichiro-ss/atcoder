# input
a, b = [int(_) for _ in input().split()]
print(b - a + 1 if b - a >= 0 else 0)