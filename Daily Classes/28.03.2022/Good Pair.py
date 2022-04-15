class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        N = len(A)
        A.sort()
        for i in range(N):
            K = B - A[i]
            status = self.binarySearch(A, K, i + 1, N - 1)
            if status != -1 and status != i:
                return 1

        return 0

    def binarySearch(self, array, x, low, high):

        while low <= high:
            mid = low + (high - low) // 2
            if array[mid] == x:
                return mid
            elif array[mid] < x:
                low = mid + 1
            else:
                high = mid - 1

        return -1


sol = Solution()
myList = [1, 2, 3, 4]

print(sol.solve(myList, 7))
