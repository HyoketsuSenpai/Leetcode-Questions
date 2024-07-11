class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = set()
        def c(i,arr):
            if len(arr) == k:
                ans.add(tuple(arr))
                return
            if i > n:
                return
            c(i + 1,arr)
            c(i + 1,arr + [i])
        c(1,[])
        return ans
            
