class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l = []
        n = len(nums)
        def bt(i,arr):
            if i == n:
                l.append(arr)
                return
            bt(i+1,arr)
            bt(i + 1,arr + [nums[i]])
        bt(0,[])
        return l
            
            
