from typing import List


# prefix Array creation
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        preFixSumArray = [nums[0]]
        for i in range(1, len(nums)):
            preFixSumArray.append(preFixSumArray[i-1] + nums[i])

        return preFixSumArray


sol = Solution()
myList = [1, 5, 2, 3, 4, 1, 2, 4]
print(sol.runningSum(myList))
