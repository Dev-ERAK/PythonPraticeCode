class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        productOfArrEle = 1

        for ele in A:
            productOfArrEle *= ele

        productArr = []

        for ele in A:
            productArr.append(productOfArrEle // ele)

        return productArr


sol = Solution()
myList = [1, 2, 3, 4, 5]
print(sol.solve(myList))
