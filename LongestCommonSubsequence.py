def lcs(str1: str, str2: str) -> int:
    l1 = len(str1)
    l2 = len(str2)

    dp = [[0 for _ in range(l2+1)] for _ in range(l1+1)]

    for i in range(l1-1, -1, -1):
        for j in range(l2-1, -1, -1):
            if str1[i] == str2[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i][j+1], dp[i+1][j])

    return dp[0][0]


print(lcs("AGGgTAB", "GgXTXAYB"))
