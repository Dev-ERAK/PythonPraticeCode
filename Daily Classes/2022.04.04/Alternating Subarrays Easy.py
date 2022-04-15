class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        state = A[0]

        N = len(A)
        outPutArr = []
        if B == 0:
            return list(range(N))

        subArrLen = 2 * B + 1
        print(subArrLen)
        start = 0
        curr = 0
        prev = A[0]
        for i in range(1, N):
            curr = i
            print("prev : " + str(prev) + ", start : " + str(start) + ", curr : " + str(curr))
            if prev ^ A[i] == 1:
                print(" XOR = 1")
                if (curr - start + 1) == subArrLen:
                    currSum = (curr * (curr + 1)) / 2
                    startSum = (start * (start - 1)) / 2
                    print("currSum : " + str(currSum) + ", startSum : " + str(startSum))
                    outPutArr.append(int((currSum - startSum) // subArrLen))
                    start += 1
                    print("appended")
            else:
                start = i
            prev = A[i]

        return outPutArr


sol = Solution()
myList = [1, 0, 1, 0, 1]
print(sol.solve(myList, 0))
