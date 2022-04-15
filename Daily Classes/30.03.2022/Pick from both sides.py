class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        total = 0
        maxSum = 0
        j = len(A) - 1
        i = 0
        bIndex = B
        for i in range(B):
            total += A[i]

        maxSum = total

        while bIndex:
            bIndex -= 1
            total -= A[bIndex]
            print(" A[j] " + str(A[j]))
            total += A[j]
            j -= 1
            maxSum = max(maxSum, total)

        return maxSum


sol = Solution()
myList = [-533, -666, -500, 169, 724, 478, 358, -38, -536, 705, -855, 281, -173, 961, -509, -5, 942, -173, 436, -609,
          -396, 902, -847, -708, -618, 421, -284, 718, 895, 447, 726, -229, 538, 869, 912, 667, -701, 35, 894, -297,
          811, 322, -667, 673, -336, 141, 711, -747, -132, 547, 644, -338, -243, -963, -141, -277, 741, 529, -222, -684,
          35]
print(sol.solve(myList, 2))
