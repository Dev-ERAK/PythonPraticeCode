class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        flagExists = 0
        totalOps = 0
        for ele in A:
            if ele == B:
                flagExists = 1

            else:
                if ele > B:
                    totalOps += 1

        if flagExists:
            return totalOps
        else:
            return -1


sol = Solution()
myList = [1, 4, 2]
print(sol.solve(myList, 3))
