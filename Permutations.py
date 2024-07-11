class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        l = set()
        n = len(nums)
        def bt(arr):
            if len(arr) == n:
                l.add(tuple(arr))
                return
            for j in range(n):
                if nums[j] not in arr:
                    bt(arr + [nums[j]])
        bt([])
        return l
