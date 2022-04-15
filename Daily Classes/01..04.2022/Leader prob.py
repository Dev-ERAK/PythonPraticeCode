class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        N = len(A)
        countLeader = []
        leader = A[N - 1]
        countLeader.append(leader)
        for i in range(N - 2, -1, -1):
            if A[i] > leader:
                leader = A[i]
                countLeader.append(leader)

        return countLeader


sol = Solution()
myList = [16, 17, 4, 3, 5, 2]
print(sol.solve(myList))
