class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):

        row = len(A)
        col = len(A[0])
        outArr = []

        for i in range(row):
            rowArr = []
            for j in range(col):
                rowArr.append(A[i][j] + B[i][j])
            outArr.append(rowArr)

        return outArr




sol = Solution()
A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
B = [[9, 8, 7],[6, 5, 4],[3, 2, 1]]
print(sol.solve(A, B))