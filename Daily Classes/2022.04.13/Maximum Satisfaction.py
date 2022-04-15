def is4SetBit(temp, A):
    N = len(A)
    count = 0
    for i in range(N):
        if A[i] & temp == temp:
            count += 1
            if count >= 4:
                return True

    return False

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        NoOfNits = 32
        ans = 0
        while NoOfNits >= 0:
            temp = ans | (1 << NoOfNits)
            if is4SetBit(temp, A):
                ans = temp
            NoOfNits -= 1
        return ans


sol = Solution()
myList = [10, 20, 15, 4, 14, 8]
print(sol.solve(myList))
