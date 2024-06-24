class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st = []
        score = 0
        cur = 0
        i = 0
        block = False
        for n in s:
            if n == '(':
                st.append('(')
                if cur == 0:
                    cur += 1
                else:
                    cur *= 2
                Block = False
            else:
                st.pop()
                if not Block:
                    score += cur
                if cur == 1:
                    cur = 0
                else:
                    cur =cur // 2
                Block = True
            
        return score

