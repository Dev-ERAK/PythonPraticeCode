class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        ans = A
        count = 0
        while ans > 0:
            if ans & 1:
                count += 1
            ans = ans >> 1

        return count


sol = Solution()
myList = 1
print(sol.solve(myList))
