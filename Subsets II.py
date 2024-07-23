class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        l = set()
        n = len(nums)
        def bt(i,arr):
            if i == n:
                arr.sort()
                l.add(tuple(arr))
                return
            bt(i + 1,arr)
            bt(i + 1,arr + [nums[i]])
        bt(0,[])
        return l

            
            
