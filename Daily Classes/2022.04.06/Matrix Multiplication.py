class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        M = len(A)
        N1 = len(A[0])
        N2 = len(B)

        if N1 != N2:
            return 0

        P = len(B[0])
        outArr = []
        for i in range(M):
            rowArr = []
            for j in range(P):
                total = 0
                for k in range(N1):
                    total += A[i][k] * B[k][j]
                rowArr.append(total)
            outArr.append(rowArr)

        return outArr


sol = Solution()
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(sol.solve(A, B))
