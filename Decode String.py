class Solution:
    def decodeString(self, s: str) -> str:
        st = ''
        def chg(num,wrd):
            t = ''
            i = 0
            while i < len(wrd):
                if wrd[i].isdigit():
                    b = 1
                    e = []
                    l = i
                    i += 2
                    while b :
                        e.append(wrd[i])
                        if wrd[i] == '[':
                            b += 1
                        if wrd[i] == ']':
                            b -= 1 
                        i += 1
                    i -= 1
                    t += chg(int(wrd[l]),['['] + e )
                    
                else:
                    t += wrd[i]
                i += 1
            return num * t
        ss = ' '
        for i in range(len(s)):
            if (ss[-1].isalpha() or ss[-1].isspace()) and s[i].isdigit():
                ss += ' '
                ss += s[i]
            elif ss[-1].isdigit() and s[i] == '[':
                ss += ' '
                ss += s[i]
                ss += ' '
            elif s[i] == ']':
                ss += ' '
                ss += s[i]
                ss += ' '
            else:
                ss += s[i]
        print(ss.split())
        r = ss.split()
        
        m = chg(1,r)
        ans = ''
        for an in m:
            if an !='[' and an != ']':
                ans += an
        return ans
