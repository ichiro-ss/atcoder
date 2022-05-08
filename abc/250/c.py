# input
n, q = [int(_) for _ in input().split()]
x = []
for _ in range(q):
    x.append(int(input()))

balls = [int(i) + 1 for i in range(n)]
place = [int(i) for i in range(n)]

for i in range(q):
    p = place[x[i] - 1]
    if p == n - 1:
        place[balls[p - 1] - 1] += 1
        place[balls[p] - 1] -= 1
        tmp = balls[p]
        balls[p] = balls[p - 1]
        balls[p - 1] = tmp
    else:
        place[balls[p] - 1] += 1
        place[balls[p + 1] - 1] -= 1
        tmp = balls[p]
        balls[p] = balls[p + 1]
        balls[p + 1] = tmp

for i in balls:
    print(i, end=" ")