class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        N = len(A)
        oddCounter = 0
        for i in range(N):
            if A[i] & 1 != 0:
                oddCounter += 1

        ans = "No" if oddCounter & 1 != 0 else "Yes"
        return ans


sol = Solution()
B = [1]
print(sol.solve(B))
