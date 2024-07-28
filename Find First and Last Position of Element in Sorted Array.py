class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1,-1]

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r)//2
            if nums[m] == target and (nums[m - 1] != target or m == 0):
                ans = [m,m]
                break
            if nums[m] >= target:
                r = m - 1
            if nums[m] < target:
                l = m + 1

        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r)//2
            if nums[m] > target:
                r = m - 1
            if nums[m] <= target:
                if nums[m] == target and (m == len(nums) - 1 or nums[m] != nums[m + 1]):
                    ans[1] = m
                    break
                l = m + 1
            

        return ans
