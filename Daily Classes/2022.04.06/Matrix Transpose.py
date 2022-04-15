class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        row = len(A)
        col = len(A[0])

        outArr = []

        for i in range(col):
            rowArr = []
            for j in range(row):
                rowArr.append(A[j][i])
            outArr.append(rowArr)

        return outArr


sol = Solution()
A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 2, 3, 4]]
print(sol.solve(A))
