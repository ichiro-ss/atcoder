n, m, k = [int(i) for i in input().split()]

# DP
dp = [[0 for i in range(k + 1)] for j in range(n + 1)]
dp[0][0] = 1

for i in range(1, n + 1):
    for j in range(k + 1):
        dp[i][j] += sum(dp[i - 1][max(0, j - m):j])
        dp[i][j] %= 998244353

print(sum(dp[n]) % 998244353)


# houjo genri