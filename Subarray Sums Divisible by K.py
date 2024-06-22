class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        pre = defaultdict(int)
        sm = 0
        md = 0
        for n in nums:
            pre[md] += 1
            sm += n
            md = sm % k
            if md < 0:
                md += k

            ans += pre[md]

        return ans
