class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        preSumArr = []
        N = len(A)
        if N > 0:
            preSumArr.append(A[0])
        print(preSumArr)
        for i in range(1, N):
            preSumArr.append(preSumArr[i - 1] + A[i])
        print(preSumArr)

        if preSumArr[N - 1] - preSumArr[0] == 0:
            return 0

        for i in range(1, N):
            if preSumArr[i - 1] == preSumArr[N - 1] - preSumArr[i]:
                return i

        return -1


sol = Solution()
myList = [49,82,85,38,89,66,51,4,31,12,33,83,29,64,78,50,25,24,27,76,59,65,41,37,6,80,61,8,48,38,85,41,18,12,81,36,37,12,44,22,65,12,33,19,42,25,30,5,4,96,81,72,71,20,20,23,85,93,33,32,30,12,97,24,13,93,58,74,37,10,46,26,21,41,92,90,21,65,35,89,26,10,14,64,28,3,80,99,62,38,55,8,92,31,93,58,77,21,34,57]
print(sol.solve(myList))
