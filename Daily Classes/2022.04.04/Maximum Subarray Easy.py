class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def maxSubarray(self, A, B, C):
        minEle = min(C)
        N = int(A)
        if B < minEle:
            return 0

        total = C[0]
        j = 0
        maxPossible = []
        for i in range(1, N + 1):

            while total > B and j < i - 1:
                total -= C[j]
                j += 1

            if total == B:
                return total
            elif total < B:
                maxPossible.append(total)

            if i < N:
                total += C[i]

        return max(maxPossible)


sol = Solution()
myList = [7, 10, 3, 1]
print(sol.maxSubarray(len(myList), 11, myList))
