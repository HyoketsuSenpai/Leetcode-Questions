class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        ln = {'2':('a','b','c'),'3':('d','e','f'),'4':('g','h','i'),'5':('j','k','l'),'6':('m','n','o'),'7':('p','q','r','s'),'8':('t','u','v'),'9':('w','x','y','z')}
        
        def bt(s,i):
            if i >= len(digits):
                if s != '':
                    ans.append(s)
                return
            
            for elem in ln[digits[i]]:
                bt(s + elem,i + 1)

        bt('',0)
        return ans
