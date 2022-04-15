class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        maxNum = max(A)
        result = 0
        for ele in A:
            result += (maxNum - ele)

        return result


sol = Solution()
myList = [2, 4, 1, 3, 2]
print(sol.solve(myList))
