class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        cnt = 0
        st = []
        for p in s:
            if p == '(':
                st.append(p)
            else:
                if st:
                    st.pop()
                else:
                    cnt += 1
        return cnt + len(st)
