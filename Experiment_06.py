#bag with limites capacity

weights = [2,3,4,5,6,7,8,9]
values = [300,400,500,600,700,800,900,1000]

capacity = 10
n = len(weights)

dp =[[0]*(capacity+1)for i in range(n+1)]

for i in range(1,n+1):
    for w in range(1,capacity+1):
        if weights[i-1] <= w:
            take = values[i-1] + dp[i-1][w - weights[i-1]]
            not_take = dp[i-1][2]
            dp [i][w] = max(take,not_take)
        else:
            dp[i][w] = dp[i-1][w]

print("Maximum value",dp[n][capacity])        