import math


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        Div = A / 200
        print(Div)
        ans = 0
        if Div < 0:
            ans = math.floor(Div) if math.ceil(Div) - 0.4999999999 >= Div else math.ceil(Div)
        else:
            ans = math.floor(Div) if math.floor(Div) + 0.4999999999 >= Div else math.ceil(Div)

        return ans


sol = Solution()
print(math.ceil(-2.25))
print(sol.solve(490))
