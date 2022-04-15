class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):

        count_A = 0
        totalPair = 0

        for ele in A:

            if "A".__eq__(ele):
                count_A += 1

            elif "G".__eq__(ele):
                totalPair += count_A

        return totalPair


sol = Solution()
myList = "ABCGAG"
print(sol.solve(myList))
