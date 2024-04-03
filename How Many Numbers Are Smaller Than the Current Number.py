class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nn = deepcopy(nums)
        nums.sort()
        n = dict()
        l = list()
        no_of_nums = len(nums)
        i = 0
        while i < no_of_nums:
            j = i
            while i < no_of_nums and nums[j] == nums[i]:
                n[nums[i]] = j
                i+=1
        for x in nn:
            l.append(n[x])
        return l
