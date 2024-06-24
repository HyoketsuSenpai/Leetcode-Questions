class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        s = []
        for c in path:
            if c != '.' and c != '':
                if c == '..':
                    if s:
                        s.pop()
                else:
                    s.append(c)
        return '/' + '/'.join(s)

                
