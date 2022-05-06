# input()
a = [int(i) for i in input().split()]

# Y dont u use sort
ans = "No"
for i in range(6):
    if a[(i + 2) % 3] - a[(i + 1) % 3] == a[(i + 1) % 3] - a[i % 3]:
        ans = "Yes"
print(ans)