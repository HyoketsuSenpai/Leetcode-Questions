class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        nums = list(set(nums))
        nums.sort()
        ll = []
        for num in nums:
            ll.append(cnt[num])
        cnt = 0
        for i in range(len(ll),1,-1):
            cnt += ll[-1]
            ll[-2] += ll[-1]
            ll.pop()
            
        return cnt
