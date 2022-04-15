class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        max_len = max(len(A), len(B))
        size_diff = abs(len(A) - len(B))
        total = ""
        carry = 0
        for i in range(max_len - 1, -1, -1):
            if i - size_diff > -1:
                numA = A[i - size_diff] if max_len > len(A) else A[i]
                numB = B[i - size_diff] if max_len > len(B) else B[i]
            else:
                numA = "0" if max_len > len(A) else A[i]
                numB = "0" if max_len > len(B) else B[i]

            print("A : " + numA + " B : " + numB)

            curr_total = int(numA) + int(numB) + carry
            print(curr_total)
            carry = curr_total // 2

            total += str(curr_total % 2)
            print(total)
        if carry == 1:
            total += "1"

        return total[::-1]


sol = Solution()
myList = "111"
B = "101"
print(sol.addBinary(myList, B))
