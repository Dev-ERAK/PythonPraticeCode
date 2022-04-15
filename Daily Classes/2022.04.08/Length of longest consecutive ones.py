class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        preArr = [int(A[0])]
        N = len(A)
        onesCounter = ord(A[0]) - 48
        for i in range(1, N):
            if A[i] == '0':
                preArr.append(0)
            else:
                print("i : " + str(i) + ": :" + str(preArr[i - 1]))
                preArr.append(preArr[i - 1] + 1)
                onesCounter += 1

        print(preArr)
        print(onesCounter)
        postFixArr = [0] * N
        postFixArr[N - 1] = int(A[N - 1])

        for i in range(N - 2, -1, -1):
            if A[i] == '0':
                postFixArr[i] = 0
            else:
                print("i : " + str(i) + ": :" + str(postFixArr[i + 1]))
                postFixArr[i] = postFixArr[i + 1] + 1

        print(postFixArr)

        ans = -float("inf")
        for i in range(N):
            if A[i] == '0':
                L = 0 if i == 0 else preArr[i - 1]
                R = 0 if i == N - 1 else postFixArr[i + 1]
                total = L + R + 1 if L + R + 1 <= onesCounter else L + R
                ans = max(ans, total)

        if ans == -float("inf"):
            return N

        return ans


sol = Solution()
A = "100001011"
print(sol.solve(A))
