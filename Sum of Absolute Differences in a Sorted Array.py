class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        l = []
        n = len(nums)
        l.append(nums[0])
        for i in range(1,n):
            l.append(l[-1] + nums[i])
        
        
        res = []
        res.append(l[-1] - n * nums[0])
        for i in range(1,n - 1):
            res.append(abs(l[i - 1] - i * nums[i]) + abs((n - i - 1) * nums[i] - (l[-1] - l[i])))
        if n > 1:
            res.append(abs(l[-2] - n * nums[-1] + nums[-1]))
        return res
