import sys


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        maxE = -sys.maxsize - 1
        minO = sys.maxsize

        for ele in A:
            print(ele)
            if ele == 0:
                continue
            elif ele % 2 == 0 and maxE < ele:
                maxE = ele
            elif ele % 2 != 0 and minO > ele:
                print(ele)
                minO = ele
        print(maxE)
        print(minO)
        return maxE - minO


sol = Solution()
myList = [-92, 22, 2, 11, 39, 36, 36, 51, 71, 42]
print(sol.solve(myList))
