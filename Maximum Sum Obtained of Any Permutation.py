class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        l = [0] * (len(nums) + 1)
        for x,y in requests:
            l[x] += 1
            l[y + 1] -= 1
        l.pop()
        
        cnt = 0

        for i in range(len(l)):
            cnt += l[i]
            l[i] = cnt
        
        nums.sort()
        l.sort()
        ans = 0
        for i in range(len(l)):
            ans += nums[i] * l[i]
        return ans % (10**9 + 7)
