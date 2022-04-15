class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        N = len(A)

        prefixSumArr = []
        if N >= 1:
            prefixSumArr.append(A[0])
        for i in range(1, N):
            prefixSumArr.append(prefixSumArr[i - 1] + A[i])

        print(prefixSumArr)
        avg = float("inf")
        total = prefixSumArr[B - 1]
        currAvg = total / B
        print(currAvg, end=" ")
        print(B - 1)
        if currAvg < avg:
            avg = currAvg
            ans = 0
        for i in range(B, N):
            total = prefixSumArr[i] - prefixSumArr[i - B]
            print(total)
            currAvg = total / B
            print(currAvg, end=" ")
            print(i)
            if currAvg < avg:
                avg = currAvg
                ans = i - B + 1

        return ans


sol = Solution()
myList = [18, 11, 16, 19, 11, 9, 8, 15, 3, 10, 9, 20, 1, 19]
print(sol.solve(myList, 1))
