class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        N = len(A)
        count = 0
        for i in range(N):
            arrsum = 0
            for j in range(i, N):
                arrsum += A[j]
                if (arrsum < B and (j - i + 1) % 2 == 0) or (arrsum > B and (j - i + 1) % 2 != 0):
                    count += 1

        return count


sol = Solution()
myList = [13, 16, 16, 15, 9, 16, 2, 7, 6, 17, 3, 9]
print(sol.solve(myList, 65))
