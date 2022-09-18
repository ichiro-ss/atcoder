n = int(input())
vec = []
for i in range(n):
    vec.append([])
    for j in range(i+1):
        if j == 0 or j == i:
            print(1, end = " ")
            vec[i].append(1)
        else:
            tmp = vec[i-1][j-1] + vec[i-1][j]
            print(tmp, end = " ")
            vec[i].append(tmp)
    print()