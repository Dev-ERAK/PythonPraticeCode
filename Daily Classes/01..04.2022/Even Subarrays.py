class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        N = len(A)

        if N % 2 != 0 or A[0] % 2 != 0 or A[N - 1] % 2 != 0:
            return "NO"

        return "YES"
        evenEleCount = 0
        i = 0
        for ele in A:
            if ele % 2 == 0:
                evenEleCount += 1
                print(str(ele) + " " + str(i))
            i += 1
        # print(evenEleCount)
        if evenEleCount % 2 == 0 or (evenEleCount % 2 == 0):
            return "YES"
        else:
            return "NO"


sol = Solution()
myList = [978, 847, 95, 729, 778, 586, 188, 782, 813, 870, 871, 940, 312, 693, 580, 101, 760, 837, 564, 633, 680, 155,
          241, 374, 682, 290, 850, 601, 433, 922, 773, 959, 530, 290, 990, 50, 516, 409, 868, 131, 664, 851, 721, 880,
          20, 450, 745, 387, 787, 823, 392, 242, 674, 347, 65, 135, 819, 324, 651, 678, 139, 940]
print(sol.solve(myList))
