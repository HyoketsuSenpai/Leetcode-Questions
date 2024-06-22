class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        pre = defaultdict(int)
        sm = 0
        cnt = 0
        for n in nums:
            pre[sm] += 1
            sm += n
            cnt += pre[sm - goal]
        return cnt
