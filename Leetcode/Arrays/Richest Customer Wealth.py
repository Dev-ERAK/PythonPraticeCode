from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        M = len(accounts)
        N = len(accounts[0])
        ans = 0
        for i in range(M):
            rowSum = 0
            for j in range(N):
                rowSum += accounts[i][j]

            ans = max(ans, rowSum)

        return ans


sol = Solution()
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(sol.maximumWealth(A))
