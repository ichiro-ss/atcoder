# input
n_order = 1000
a, b, c, d = [0]*n_order, [0]*n_order, [0]*n_order,  [0]*n_order
for i in range(n_order):
    a[i], b[i], c[i], d[i] = [int(_) for _ in input().split()]

def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

visited = [False for _ in range(n_order)]
footprints = [[400, 400]]
orders = []

now_x, now_y, now_i = 400, 400, -1
for _ in range(50):
    min_i, min_d = 0, 10 ** 6
    for i in range(n_order):
        if visited[i]:
            continue
        now_d = dist(a[i], b[i], now_x, now_y)
        if now_d < min_d:
            min_i = i
            min_d = now_d
    now_i = min_i
    now_x, now_y = a[now_i], b[now_i]
    footprints.append([now_x, now_y])
    orders.append(now_i)
    visited[now_i] = True

deliverd = [False for _ in range(len(orders))]
for _ in orders:
    min_i, min_d = 0, 10 ** 6
    for i in range(len(orders)):
        if deliverd[i]:
            continue
        now_d = dist(c[orders[i]], d[orders[i]], now_x, now_y)
        if now_d < min_d:
            min_i = i
            min_d = now_d
    now_i = min_i
    now_x, now_y = c[orders[now_i]], d[orders[now_i]]
    footprints.append([now_x, now_y])
    deliverd[now_i] = True
footprints.append([400, 400])

# output
print(len(orders), end = " ")
for v in orders:
    print(v + 1, end = " ")
print("")

print(len(footprints), end = " ")
for fx, fy in footprints:
    print(fx, fy, end = " ")
