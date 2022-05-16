from itertools import permutations
# input
n, m = [int(_) for _ in input().split()]
a = [[int(_) - 1 for _ in input().split()] for _ in range(m)]
c = [[int(_) - 1 for _ in input().split()] for _ in range(m)]

c_edges = [[False for _ in range(n)] for _ in range(n)]
for i in range(m):
    c_edges[c[i][0]][c[i][1]] = True
    c_edges[c[i][1]][c[i][0]] = True
    c_edges[c[i][0]][c[i][1]] = True
    c_edges[c[i][1]][c[i][0]] = True

ans = "No"
v_change = permutations(list(range(n)))
for v_list in v_change:
    a_edges = [[False for _ in range(n)] for _ in range(n)]
    for i in range(m):
        a_edges[v_list[a[i][0]]][v_list[a[i][1]]] = True
        a_edges[v_list[a[i][1]]][v_list[a[i][0]]] = True
        a_edges[v_list[a[i][0]]][v_list[a[i][1]]] = True
        a_edges[v_list[a[i][1]]][v_list[a[i][0]]] = True
    if a_edges == c_edges:
        ans = "Yes"
print(ans)