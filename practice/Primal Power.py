import math


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        N = len(A)
        print(N)
        primeCounter = 0
        for i in range(N):
            if A[i] > 1 and self.isPrime(A[i]):
                primeCounter += 1
                print(str(primeCounter) + " " + str(A[i]))

        return primeCounter

    def isPrime(self, N):

        for i in range(2, int(math.sqrt(N)) + 1):
            if N % i == 0:
                return False
        return True


sol = Solution()
B = [97, 43, 29, 11, 100, 47, 76, 83, 37, 19, 17, 19, 71, 0, 1, -82, 2, -83, 37, 13, 5, 97, 17, 30, 31, 48, 2, 19, 31,
     91, 19, 2, 5, 89, 2, 67, 31, 47, 43, 31, 5, 17, 83, 11, 47, 73, 19, 3, 3, 19, 59, 91, 67, 7, 43, 4, 3, 51, 52, 23,
     3, 37, 53, 89, 9, 41, 19, 61, 7, 5, 53, 59, 19, 11, 79, 37, 31, 37, 73, 82, 41, 2, 13, 8, 2, 36, 19, 58, 17, 17,
     59, 59, 37, 11, 13, 37, 47, 83, 31, 3]
print(sol.solve(B))
