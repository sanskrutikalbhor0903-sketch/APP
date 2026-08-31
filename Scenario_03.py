# Climbing Stairs Problem using Dynamic Programming

n = int(input("Enter the number of stairs: "))

if n <= 0:
    ways = 0
elif n == 1:
    ways = 1
else:
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    ways = dp[n]

print("Total number of ways:", ways)