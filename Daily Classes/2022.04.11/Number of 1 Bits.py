class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):

        bitCounts = 0

        while A != 0:
            if A & 1:
                bitCounts += 1
            A = A >> 1

        return bitCounts


sol = Solution()
B = 12
print(sol.numSetBits(B))
