# this is ahc006 playground
# first, modified ahc006 nearest neighbor algorithm so that
# he can deliver orders once the order is received
# In short, allow orders to be delivered before all orders are received

import statistics
# input
n_order = 1000
a, b, c, d = [0]*n_order, [0]*n_order, [0]*n_order,  [0]*n_order
for i in range(n_order):
    a[i], b[i], c[i], d[i] = [int(_) for _ in input().split()]

def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

visited = [False for _ in range(n_order)]
deliverd = [False for _ in range(50)]
footprints = [[400, 400]]
orders = []

# remove distant points 
removed = [False for _ in range(n_order)]
ab_dist = [0] * n_order
for i in range(n_order):
    ab_dist[i] = dist(400, 400, a[i], b[i])
med_ab_dist = statistics.median(ab_dist)
for i in range(n_order):
    if ab_dist[i] > med_ab_dist:
        removed[i] = True

cd_dist = [0] * n_order
for i in range(n_order):
    cd_dist[i] = dist(400, 400, c[i], d[i])
med_cd_dist = statistics.median(cd_dist)
for i in range(n_order):
    if cd_dist[i] > med_cd_dist:
        removed[i] = True
    

now_x, now_y, now_i = 400, 400, -1
while len(orders) < 50:
    min_i, min_d = 0, 10 ** 6
    receiving = True
    for i in range(n_order):
        if visited[i] or removed[i]:
            continue
        now_d = dist(a[i], b[i], now_x, now_y)
        if now_d < min_d:
            min_i = i
            min_d = now_d
    for i in range(len(orders)):
        if deliverd[i]:
            continue
        now_d = dist(c[orders[i]],d[orders[i]], now_x, now_y)
        if now_d < min_d:
            min_i = i
            min_d = now_d
            receiving = False
    if receiving:
        now_i = min_i
        now_x, now_y = a[now_i], b[now_i]
        footprints.append([now_x, now_y])
        orders.append(now_i)
        visited[now_i] = True
    else:
        now_i = min_i
        now_x, now_y = c[orders[now_i]], d[orders[now_i]]
        footprints.append([now_x, now_y])
        deliverd[now_i] = True

while not all(deliverd):
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
