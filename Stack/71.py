class Solution:
    def simplifyPath(self, path: str) -> str:
        #edge case
        if not path:
            return ""
        
        stack = []
        
        #parameter
        for splitstr in path.split("/"):
            if splitstr == (".."):
                if stack:
                    stack.pop()
            elif splitstr == (".") or splitstr == (""):
                continue
            else:
                stack.append(splitstr)
        
        return "/" + "/".join(stack)