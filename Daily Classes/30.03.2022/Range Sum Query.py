class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return an list of long
    def rangeSum(self, A, B):
        preSumArr = []
        outPutArr = []
        N = len(A)
        if N > 0:
            preSumArr.append(A[0])
        for i in range(1, N):
            preSumArr.append(preSumArr[i - 1] + A[i])
        print(preSumArr)
        for eleArr in B:
            if eleArr[0] == 1:
                outPutArr.append(preSumArr[eleArr[1] - 1])
            else:
                outPutArr.append(preSumArr[eleArr[1] - 1] - preSumArr[eleArr[0] - 2])

        return outPutArr


sol = Solution()
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
myQueries = [[1, 1], [2, 3], [4, 8]]

print(sol.rangeSum(myList, myQueries))
