class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        row = len(A)
        col = len(A[0])
        outArr = []

        for i in range(row):
            total = 0
            for j in range(col):
                total += A[i][j]

            outArr.append(total)

        return outArr


sol = Solution()
A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 2, 3, 4]]
print(sol.solve(A))
