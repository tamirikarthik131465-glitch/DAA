
def making_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], 1 + dp[i - coin])

    if dp[amount] == float('inf'):
        return -1

    return dp[amount]


n = int(input("Enter number of coin types: "))

coins = []

for i in range(n):
    coin = int(input("Enter coin value: "))
    coins.append(coin)

amount = int(input("Enter amount: "))

result = making_change(coins, amount)

if result == -1:
    print("Change cannot be made")
else:
    print("Minimum number of coins =", result)

print("Time Complexity: O(n * amount)")
print("Space Complexity: O(amount)")
