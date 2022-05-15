# input
n = int(input())
people = {}
for _ in range(n):
    s = str(input())
    if s not in people:
        people[s] = 1
    else:
        people[s] += 1

print(max(people.items(), key = lambda x:x[1])[0])