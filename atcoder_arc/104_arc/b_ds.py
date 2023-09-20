#input
n, s = [i for i in input().split()]

n = int(n)
continuation = 1
cnt = 0
for i in range(n - 1):
    if (s[i] == 'A' and s[i+1] == 'T') or (s[i] == 'T' and s[i+1] == 'A')\
        or (s[i] == 'C' and s[i+1] == 'G') or (s[i] == 'G' and s[i+1] == 'C'):
        cnt += 1
        continuation += 1
        if continuation % 2 and continuation != 2:
            cnt += 1
    else:
        continuation = 1
print(cnt)