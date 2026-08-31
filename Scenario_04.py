str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

m = len(str1)
n = len(str2)

dp = [[0] * (n + 1) for i in range(m + 1)]

maximum = 0

for i in range(1, m + 1):
    for j in range(1, n + 1):

        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = 1 + dp[i - 1][j - 1]

            if dp[i][j] > maximum:
                maximum = dp[i][j]

        else:
            dp[i][j] = 0

print("Length of longest common substring:", maximum)