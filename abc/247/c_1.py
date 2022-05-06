n = int(input())

def sol(n, x):
    if n == 1:
        return '1'
    else:
        x = sol(n - 1, x) + ' ' + str(n) + ' ' + sol(n - 1, x)
        n -= 1
    return x

x = str(n)
x = sol(n, x)
print(x)