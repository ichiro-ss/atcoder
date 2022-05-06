import bisect
# def bins(a, x):
#     l, r = 0, len(a) - 1
#     while l < r:
#         mid = l + (r - l) // 2
#         if x == a[mid]:
#             return mid
#             exit()
#         elif x < a[mid]:
#             r = mid
#         else:
#             l = mid + 1
#         return r

# def bins_eq(a, x):
#     l, r = 0, len(a) - 1
#     while l < r:
#         mid = l + (r - l) // 2
#         if x == a[mid]:
#             return mid
#             exit()
#         elif x < a[mid]:
#             r = mid - 1
#         else:
#             l = mid
#         return l

n = int(input())
a = [int(i) for i in input().split()]
idxs = {}
for i in range(n):
    if a[i] not in idxs:
        idxs[a[i]] = [i + 1]
    else:
        idxs[a[i]].append(i + 1)

q = int(input())
for _ in range(q):
    l, r, x = [int(i) for i in input().split()]
    if x not in idxs:
        print(0)
    else:
        # 1 brute force
        # cnt = 0
        # for val in idxs[x]:
        #     if l <= val <= r:
        #         cnt += 1
        # print(cnt)

        # 2 binary search
        print(bisect.bisect_right(idxs[x], r) - bisect.bisect_left(idxs[x], l))
