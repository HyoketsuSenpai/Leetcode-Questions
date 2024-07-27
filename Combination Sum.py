class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def bt(beg,arr,sm):
            if sm > target:
                return
            if sm == target:
                ans.append(arr)
                return
            for i in range(beg,len(candidates)):
                bt(i,arr + [candidates[i]],sm + candidates[i])
        for i in range(len(candidates)):
            bt(i,[candidates[i]],candidates[i])
        return ans
