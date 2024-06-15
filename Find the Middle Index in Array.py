class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        lv = 0
        lr = sum(nums) - nums[0]

        if lv == lr:
                return 0

        for i in range(1,len(nums)):
            
            lr -= nums[i]
            lv += nums[i - 1]

            if lv == lr:
                return i

        return -1
