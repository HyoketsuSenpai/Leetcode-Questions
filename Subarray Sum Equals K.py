class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        sm = 0
        sums =  defaultdict(int)
        for i in range(len(nums)):
            sm += nums[i]
            cnt += sums[sm - k]
            if sm == k:
                cnt += 1
            sums[sm] += 1
            
            
        return cnt
