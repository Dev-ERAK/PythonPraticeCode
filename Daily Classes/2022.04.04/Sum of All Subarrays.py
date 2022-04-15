class Solution:
    # @param A : list of integers
    # @return an long
    def subarraySum(self, A):
        total = 0
        N = len(A)
        for i in range(N):
            total += A[i] * (N-i) * (i + 1)
        return total


sol = Solution()
myList = [1, 2, 3]
print(sol.subarraySum(myList))
