import bisect
# input
q = int(input())

exist = []
cnts = {}

for _ in range(q):
    query = [int(_) for _ in input().split()]
    if query[0] == 1:
        if query[1] in cnts:
            if cnts[query[1]] == 0:
                bisect.insort(exist, query[1])
            cnts[query[1]] += 1
        else:
            cnts[query[1]] = 1
            bisect.insort(exist, query[1])
    elif query[0] == 2:
        if query[1] in cnts:
            cnts[query[1]] -= min(query[2], cnts[query[1]])
            if cnts[query[1]] == 0:
                exist.remove(query[1])
    elif query[0] == 3:
        print(exist[-1] - exist[0])
