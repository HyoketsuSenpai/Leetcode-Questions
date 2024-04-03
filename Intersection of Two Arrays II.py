class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        l = list()
        i = len(nums1)
        m = len(nums2)
        k = 0
        j = 0
        while j < i and k < m:
            while j < i and k < m and nums1[j] < nums2[k]:
                j += 1
            while j < i and k < m and nums1[j] > nums2[k]:
                k += 1
            while j < i and k < m and nums1[j] == nums2[k]:
                l.append(nums1[j])
                k+=1
                j+=1
        return l
