# input
n = int(input())
a = [int(_) for _ in input().split()]

INF = 10 ** 9 + 1

dp = [[0 for _ in range(2)] for _ in range(n)]
# without using a0
dp[0][1] = INF
for i in range(1, n):
    dp[i][0] = dp[i-1][1]
    dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + a[i]
didnt_buy_4_1 = dp[n-1][1]

# using a0
dp[0][0] = INF; dp[0][1] = a[0]
for i in range(1, n):
    dp[i][0] = dp[i-1][1]
    dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + a[i]
print(min(min(dp[n-1][0], dp[n-1][1]), didnt_buy_4_1))
