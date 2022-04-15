class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        arrXOR = 0

        for i in range(len(A)):
            arrXOR = arrXOR ^ A[i]

        print(arrXOR)
        num = arrXOR
        ithBit = 0
        while num > 0:
            if num & 1:
                break
            ithBit += 1
            num = num >> 1
        print(ithBit)
        num1, num2 = 0, 0
        for i in range(len(A)):
            if A[i] & (1 << ithBit) == 0:
                num2 = num2 ^ A[i]
            else:
                num1 = num1 ^ A[i]
        results = [num1, num2]
        results.sort()
        return results


sol = Solution()
myList = [1, 5, 2, 3, 4, 1, 2, 4]
print(sol.solve(myList))
