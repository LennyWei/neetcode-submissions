class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = [s[0]]

        for i in s[1:]:
            match i:
                case "}":
                    if len(stack) == 0 or stack.pop() != "{":
                        return False
                case "]":
                    if len(stack) == 0 or stack.pop() != "[":
                        return False
                case ")":
                    if len(stack) == 0 or stack.pop() != "(":
                        return False
                case _:
                    stack.append(i)
        
        return True if len(stack) == 0 else False 
                
