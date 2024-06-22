class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        post = [1]

        for n in nums:
            pre.append(pre[-1] * n)
        pre.pop()
        for n in nums[::-1]:
            post.append(post[-1] * n)
        post.pop()
        post.reverse()
        
        return [post[i] * pre[i] for i in range(len(nums))]
