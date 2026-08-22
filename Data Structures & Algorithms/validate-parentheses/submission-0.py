class Solution:
    def isValid(self, s: str) -> bool:
        # use a stack
        # if opening bracket, add to stack
        # if closing bracket, pop from stack, bracket should be corresponding bracket for opening bracket
        # at the end, if the stack isn't empty, then it is invalid

        brackets = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        bracketStack = []

        for char in s:
            if char in brackets.values():
                bracketStack.append(char)
            else:
                if len(bracketStack) > 0:
                    top = bracketStack.pop()
                    corrBracket = brackets[char]
                    if corrBracket != top:
                        return False
                else:
                    return False
            
        if len(bracketStack) > 0:
            return False
        
        return True

                