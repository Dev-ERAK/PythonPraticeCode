class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        countOfBits = 0
        num = A
        ans = A
        reverseNum = 0
        while num != 0:
            countOfBits += 1
            num = num >> 1

        print(countOfBits)

        for i in range(countOfBits - 1, -1, -1):
            reverseNum += (ans & 1) * 2 ** i
            ans = ans >> 1

        print(reverseNum)

        while countOfBits < 32:
            reverseNum = reverseNum << 1
            countOfBits += 1
        print(countOfBits)
        return reverseNum


sol = Solution()
B = 2
print(sol.reverse(B))
