from collections import deque

q = int(input())
cylinder = deque()
for _ in range(q):
    # input a query
    query = [int(i) for i in input().split()]
    # if query[0] equals 1, input it to the cylinder
    if query[0] == 1:
        cylinder.append([query[1], query[2]])

    # if query[0] equals 2, output the ball
    elif query[0] == 2:
        ans = 0
        # if query's demand is more than a top of cylinder, pop the top of cylinder
        while cylinder[0][1] < query[1]:
            c = cylinder.popleft()
            ans += c[0] * c[1]
            query[1] -= c[1]
        # if query's demand is less than a top of cylinder, pull it
        cylinder[0][1] -= query[1]
        ans += cylinder[0][0] * query[1]
        print(ans)