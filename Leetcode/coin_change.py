from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        n = amount + 1
        m = len(coins)
        
        dp = [[0 for j in range(n)] for i in range(m)]
        
        for i in range(m):
            for j in range(1, n):
                coin = coins[i]
                if j < coin:
                    if i == 0:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i-1][j]
                else:
                    val = j-coin
                    if val == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = (1 + dp[i][val]) if dp[i][val] != 0 else 0

        for row in dp:           
            print(row[-1])

        result = max_val = 1000000000000
        for i in range(m):
            if dp[i][-1] != 0:
                result = min(result, dp[i][-1])
        return result if result != max_val else -1

if __name__ == "__main__":
    coins = [186,419,83,408]
    amount = 6249

    sol = Solution()
    coins.sort()
    ans = sol.coinChange(coins, amount)
    print(ans)