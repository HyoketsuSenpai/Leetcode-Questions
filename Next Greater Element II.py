class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        mx = max(nums)
        done = set()
        n = [[i,x] for i,x in enumerate(nums)]
        for i in range(len(nums)):
            if nums[i] == mx:
                ans[i] = -1
                done.add(i)
        st = []
        i = 0
        while len(done) != len(nums):
            while st and st[-1][1] < nums[i]:
                j,x = st.pop()
                ans[j] = nums[i]
                done.add(j)
            if i not in done:
                st.append(n[i])
            i+=1
            i %= len(nums)
        return ans
