class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):

        rowA = len(A)
        colA = len(A[0])
        rowB = len(B)
        colB = len(B[0])

        if rowA != rowB or colA != colB:
            return 0

        for i in range(rowA):
            for j in range(colA):
                if A[i][j] != B[i][j]:
                    return 0

        return 1


sol = Solution()
A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 2, 3, 4]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
print(sol.solve(A,A))
