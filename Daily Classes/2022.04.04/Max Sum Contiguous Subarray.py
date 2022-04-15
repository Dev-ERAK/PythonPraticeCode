class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        N = len(A)
        maxi_end = 0
        maxi_till = -float("inf")
        for i in range(N):
            maxi_end += A[i]
            maxi_till = max(maxi_end, maxi_till)

            if maxi_end < 0:
                maxi_end = 0

        return maxi_till


sol = Solution()
myList = [1, 2, 3, 4, -10]
print(sol.maxSubArray(myList))
