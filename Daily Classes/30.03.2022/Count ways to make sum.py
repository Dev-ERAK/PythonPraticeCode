class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        sumO = 0
        sumE = 0
        N = len(A)
        for i in range(N):
            if i % 2 == 0:
                sumE += A[i]
            else:
                sumO += A[i]

        print(sumO)
        print(sumE)

        currOS = 0
        currES = A[0]
        totalCount = 0
        newOS = 0
        newES = 0

        if sumO == sumE - A[0]:
            totalCount += 1

        for i in range(1, N - 1):
            if i % 2 == 0:
                currES += A[i]
                newOS = currOS + sumE - currES
                newES = currES + sumO - currOS - A[i]
            else:
                currOS += A[i]
                newOS = currOS + sumE - currES - A[i]
                newES = currES + sumO - currOS
            print(" newES : " + str(newES))
            print(" newOS : " + str(newOS))
            if newES == newOS:
                totalCount += 1

        if N % 2 == 0 and sumE == sumO - A[N - 1]:
            totalCount += 1

        elif sumO == sumE - A[N - 1]:
            totalCount += 1

        return totalCount


sol = Solution()
# myList = [1, 1, 1]
myList = [1, 2, 3, 7, 1, 2, 3]
# myList = [49,82,85,38,89,66,51,4,31,12,33,83,29,64,78,50,25,24,27,76,59,65,41,37,6,80,61,8,48,38,85,41,18,12,81,36,37,12,44,22,65,12,33,19,42,25,30,5,4,96,81,72,71,20,20,23,85,93,33,32,30,12,97,24,13,93,58,74,37,10,46,26,21,41,92,90,21,65,35,89,26,10,14,64,28,3,80,99,62,38,55,8,92,31,93,58,77,21,34,57]
print(sol.solve(myList))
