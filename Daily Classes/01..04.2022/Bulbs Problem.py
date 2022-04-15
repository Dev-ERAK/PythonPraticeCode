class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        N = len(A)

        state = 0
        ans = 0
        for i in range(N):

            if state == A[i]:
                ans += 1
                state = 1 - state

        return ans


sol = Solution()
myList = [0, 1, 0, 1, 0, 1]
print(sol.bulbs(myList))
