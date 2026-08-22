class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # use a stack
        # put in 2 numbers
        # 3rd is operator
        # perform arithmetic
        # push onto stack
        # push next num onto stack

        tokensStack = []
        operators = ["+", "-", "*", "/"]

        # if i div 2 = 
        # 0 -> number
        # 1 -> operator

        for i in range(0, len(tokens)):
            if tokens[i] in operators:
                # pop the last 2 numbers
                # do the operation on them
                # push the result onto the stack
                topNum = tokensStack.pop()
                bottomNum = tokensStack.pop()
                match tokens[i]:
                    case "+":
                        result = int(topNum) + int(bottomNum)
                    case "-":
                        result = int(bottomNum) - int(topNum)
                    case "*":
                        result = int(bottomNum) * int(topNum)
                    case "/":
                        result = int(bottomNum) / int(topNum)
                
                tokensStack.append(int(result))

            else:
                tokensStack.append(tokens[i])
        
        # the final result should be the first element in the stack
        return int(tokensStack[0])