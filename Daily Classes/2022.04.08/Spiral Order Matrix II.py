class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        N = A
        spiralMat = [[0] * N for _ in range(N)]

        num = 0
        i, j = 0, 0
        while N > 1:
            num = self.addLegs(num, spiralMat, N, i, j)
            i += 1
            j += 1
            N = N-2

        if N % 2 != 0:
            spiralMat[A//2][A//2] = A**2

        return spiralMat

    def addLegs(self, num, Sp, N, i, j):

        for _ in range(N - 1):
            num += 1
            Sp[i][j] = num
            j += 1

        for _ in range(N - 1):
            num += 1
            Sp[i][j] = num
            i += 1

        for _ in range(N - 1):
            num += 1
            Sp[i][j] = num
            j -= 1

        for _ in range(N - 1):
            num += 1
            Sp[i][j] = num
            i -= 1

        return num


sol = Solution()
A = 5
print(sol.generateMatrix(A))
