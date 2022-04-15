class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        N = len(A)

        ans = 0

        for i in range(N):
            if A[i] == 'a' or A[i] == 'A' or A[i] == 'E' or A[i] == 'e' or A[i] == 'I' or A[i] == 'i' or A[i] == 'O' or \
                    A[i] == 'o' or A[i] == 'U' or A[i] == 'u':
                ans += (N - i)

        return ans % 10003


sol = Solution()
myList = "ABECFJKDGAKJ I;OUTERWUYOPBKJZXBCJK KJ IJCZXGFVUISAGSHKVHJZXJHVJL KHXHLKN FLC';SK;LJ;LC"
print(sol.solve(myList))
