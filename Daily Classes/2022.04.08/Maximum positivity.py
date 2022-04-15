class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        N = len(A)
        start = 0
        count = 0
        indexStart = float("inf")
        indexCount = -float("inf")
        for i in range(N + 1):
            if i < N and A[i] > -1:
                count += 1
            else:
                if count != 0 and count > indexCount:
                    indexCount = count
                    indexStart = start
                start = i + 1
                count = 0

        if start == N:
            return A

        return A[indexStart:indexStart + indexCount]


sol = Solution()
myList = [ 8986143, -5026827, 5591744, 4058312, 2210051, 5680315, -5251946, -607433, 1633303, 2186575 ]
print(sol.solve(myList))
