class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = list()
        candidates.sort()
        lc = len(candidates)
        def bt(beg,arr,sm):
            if sm >= target:
                if sm == target:
                    ans.append(arr)
                return
            if beg >= lc:
                return
            
            for i in range(beg,lc):
                if i > beg and candidates[i] == candidates[i - 1]:
                    continue
                
                bt(i + 1,arr + [candidates[i]],sm + candidates[i])

        bt(0,[],0)
        return ans
