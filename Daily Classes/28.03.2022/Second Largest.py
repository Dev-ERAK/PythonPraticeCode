class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        A.sort()
        N = len(A)
        if N <= 1:
            return -1
        return A[N - 2]


sol = Solution()
myList = [1, 2, 3, 7, 1, 2, 3]
print(sol.solve(myList))
