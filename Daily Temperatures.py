class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = [[i,x] for i,x in enumerate(temperatures)]
        st = []
        ans = [0] * len(temperatures)

        for n in l:
            while st and st[-1][1] < n[1]:
                i,x = st.pop()
                ans[i] = n[0] - i

            st.append(n)
        return ans
