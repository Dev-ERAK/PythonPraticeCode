class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        M = len(A)
        N = len(A[0])

        outArr = []
        row = 0
        col = 0

        while row < M:
            rowArr = [0] * N
            print("row : " + str(row) + " col : " + str(col))
            i = row
            j = col
            rowArrCount = 0
            while i < M and j >= 0:
                print("i : " + str(i) + " j : " + str(j))
                print(A[i][j])
                rowArr[rowArrCount] = A[i][j]
                rowArrCount += 1
                i += 1
                j -= 1

            if col < N - 1:
                col += 1
            else:
                row += 1
            outArr.append(rowArr)
        return outArr


sol = Solution()
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(sol.diagonal(A))
