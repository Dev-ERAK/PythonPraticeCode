from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        outArr = []
        for i in range(len(nums)):
            outArr.append(nums[i])

        for i in range(len(nums)):
            outArr.append(nums[i])
        return outArr


sol = Solution()
myList = [1, 5, 2, 3, 4, 1, 2, 4]
print(sol.getConcatenation(myList))
