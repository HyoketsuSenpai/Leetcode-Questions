class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = []
        ans = []
        i = 0
        j = 0
        s = Counter(nums1)
        d = defaultdict(deque)
        
        
        while j < len(nums2):
            
                
            while l and nums2[j] > l[-1]:
                d[l.pop()].append(nums2[j])
            l.append(nums2[j])
            if nums2[j] in s:
                s[nums2[j]]-=1
                if s[nums2[j]] == 0:
                    s.pop(nums2[j])
            else:
                l.pop()
            
                
            j += 1
        while l:
            d[l.pop()].append(-1)

        for n in nums1:
            ans.append(d[n].popleft())            
        return ans
