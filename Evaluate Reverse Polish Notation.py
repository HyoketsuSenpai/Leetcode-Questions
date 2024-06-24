class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def op(n1,n2,op):
            n1 = int(n1)
            n2 = int(n2)
            if op == '+':
                return n1 + n2
            if op == '-':
                return n1 - n2
            if op == '*':
                return n1 * n2
            if op == '/':
                
                return int(n1/n2)
        s = []
        ope = {'+','-','*','/'}
        for n in tokens:
            if n not in ope:
                s.append(n)
            else:
                a = s.pop()
                b = s.pop()
                s.append(op(b,a,n))
        return int(s[0])
            
