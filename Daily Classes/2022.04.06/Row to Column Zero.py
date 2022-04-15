class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        row = len(A)
        col = len(A[0])
        rowZeroth = False

        for r in range(row):
            for c in range(col):
                if A[r][c] == 0:
                    A[0][c] = 0

                    if r > 0:
                        A[r][0] = 0
                    else:
                        rowZeroth = True
        print(A)
        for r in range(1, row):
            for c in range(1, col):
                if A[r][0] == 0 or A[0][c] == 0:
                    A[r][c] = 0
        print(A)
        if A[0][0] == 0:
            for r in range(row):
                A[r][0] = 0
        print(A)
        if rowZeroth:
            for c in range(col):
                A[0][c] = 0

        return A


A = [
  [51, 21, 90, 38, 57, 12, 11, 1, 68, 60],
  [81, 24, 63, 97, 75, 70, 23, 91, 39, 84],
  [0, 21, 97, 12, 46, 48, 50, 3, 57, 69],
  [44, 8, 42, 34, 99, 0, 98, 10, 53, 67],
  [23, 34, 43, 86, 31, 18, 9, 54, 61, 48],
  [90, 61, 21, 87, 26, 67, 88, 28, 70, 45],
  [98, 14, 5, 92, 1, 4, 44, 99, 67, 98],
  [18, 42, 32, 61, 80, 64, 32, 89, 70, 93],
  [89, 61, 7, 10, 0, 85, 29, 40, 13, 0],
  [85, 63, 66, 43, 56, 67, 99, 0, 67, 66]
]

sol = Solution()
print(sol.solve(A))
