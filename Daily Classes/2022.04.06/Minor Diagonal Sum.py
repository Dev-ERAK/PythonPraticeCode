class Solution:
    # @param A : tuple of list of integers
    # @return an integer
    def solve(self, A):
        M = len(A)
        row = 0
        col = M - 1
        digTotal = 0
        while row < M:
            digTotal += A[row][col]
            col -= 1
            row += 1

        return digTotal


sol = Solution()
A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 2, 3, 4]]
print(sol.solve(A))
