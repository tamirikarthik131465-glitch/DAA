
def matrix_chain_order(p, n):
    dp = [[0 for i in range(n)] for j in range(n)]

    for length in range(2, n):
        for i in range(1, n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')

            for k in range(i, j):
                cost = (dp[i][k] + dp[k + 1][j] +
                        p[i - 1] * p[k] * p[j])

                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[1][n - 1]


n = int(input("Enter number of matrices: "))

p = []

for i in range(n + 1):
    x = int(input("Enter dimension: "))
    p.append(x)

result = matrix_chain_order(p, n + 1)

print("Minimum number of multiplications =", result)
print("Time Complexity: O(n^3)")
print("Space Complexity: O(n^2)")
