# input
n_order = 1000
a, b, c, d = [0]*n_order, [0]*n_order, [0]*n_order,  [0]*n_order
for i in range(n_order):
    a[i], b[i], c[i], d[i] = [int(_) for _ in input().split()]

visited = [False for _ in range(n_order)]

def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def min_dist_idx(xs, ys, now_x, now_y, judge):
    min_i, min_d = 0, 10 ** 6
    for i in range(len(xs)):
        if judge[i]:
            continue
        now_d = dist(xs[i], ys[i], now_x, now_y)
        if now_d < min_d:
            min_i = i
            min_d = now_d
    return min_i

stores = []
now_x, now_y, now_i = 400, 400, -1
for _ in range(50):
    now_i = min_dist_idx(a, b, now_x, now_y, visited)
    now_x, now_y = a[now_i], b[now_i]
    stores.append(now_i)
    visited[now_i] = True

houses = []
deliverd = [False for _ in range(50)]
for order in stores:
    min_i, min_d = 0, 10 ** 6
    for i in range(len(stores)):
        if deliverd[i]:
            continue
        now_d = dist(c[stores[i]], d[stores[i]], now_x, now_y)
        if now_d < min_d:
            min_i = i
            min_d = now_d
    now_i = min_i
    now_x, now_y = c[stores[now_i]], d[stores[now_i]]
    houses.append(now_i)
    deliverd[now_i] = True

# output
print(len(stores), end = " ")
for order in stores:
    print(order + 1, end = " ")
print("")
print(len(stores) * 2 + 2, end = " ")
print(400, 400, end = " ")
for order in stores:
    print(a[order], b[order], end = " ")
for place in houses:
    print(c[stores[place]], d[stores[place]], end = " ")
print(400, 400, end = " ")
