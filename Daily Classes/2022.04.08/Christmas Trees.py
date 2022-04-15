class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        N = len(A)

        dp = [float("inf")] * N

        ans = float("inf")

        for i in range(N):
            for j in range(i + 1, N):

                if A[j] > A[i]:
                    dp[j] = min(dp[j], B[i] + B[j])
                    ans = min(ans, dp[i] + B[j])

        if ans == float("inf"):
            return -1

        return ans


sol = Solution()
myList = [1, 6, 4, 2, 6, 9]
B = [2, 5, 7, 3, 2, 7]
print(sol.solve(myList, B))
