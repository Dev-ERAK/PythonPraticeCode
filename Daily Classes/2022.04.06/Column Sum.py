class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        row = len(A)
        col = len(A[0])
        outArr = [0] * col

        for i in range(row):
            for j in range(col):
                outArr[j] += A[i][j]

        return outArr


sol = Solution()
A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 2, 3, 4]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
print(sol.solve(A))
