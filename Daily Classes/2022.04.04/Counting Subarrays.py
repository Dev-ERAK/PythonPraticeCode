class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        N = len(A)
        count = 0
        for i in range(N):
            arrSum = 0
            for j in range(i, N):
                arrSum += A[j]
                if arrSum < B:
                    count += 1

        return count


sol = Solution()
myList = [8, 5, 1, 10, 5, 9, 9, 3, 5, 6, 6, 2, 8, 2, 2, 6, 3, 8, 7, 2, 5, 3, 4, 3, 3, 2, 7, 9, 6, 8, 7, 2, 9, 10, 3, 8,
          10, 6, 5, 4, 2, 3, 4, 4, 5, 2, 2, 4, 9, 8, 5]
print(sol.solve(myList, 32))