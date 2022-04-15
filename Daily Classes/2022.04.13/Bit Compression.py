class Solution:
    # @param A : list of integers
    # @return an integer
    def compressBits(self, A):
        N = len(A)
        if N == 1:
            return A[0]
        compressArr = [0] * N
        j = 0
        compressArr[0] = A[0]
        for i in range(N):
            j += 1

            if j == N:
                break
            print(" i : " + str(i) + " j : " + str(j) + " compressArr[i] : " + str(compressArr[i]) + " A[j] : " + str(A[j]))
            temp = compressArr[i]
            compressArr[i] = temp & A[j]
            compressArr[j] = temp | A[j]
        print(compressArr)

        xorAns = 0
        for i in range(N):
            xorAns ^= compressArr[i]

        return xorAns


sol = Solution()
myList = [1, 3, 5]
print(sol.compressBits(myList))
