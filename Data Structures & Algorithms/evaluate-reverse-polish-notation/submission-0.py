class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        '''
        pass through the array.
        add numbers, when you find a operation char, pop the previous two numbers, evaluate and push
        the resulting number 
        '''
        stack = []

        for i in tokens:

            match i:
                case "+":
                    right = stack.pop()
                    left = stack.pop()
                    stack.append(left + right)
                case "*":
                    right = stack.pop()
                    left = stack.pop()
                    stack.append(left * right)
                case "-":
                    right = stack.pop()
                    left = stack.pop()
                    stack.append(left - right)
                case "/":
                    right = stack.pop()
                    left = stack.pop()
                    stack.append(int(left / right))
                case _:
                    stack.append(int(i))
        
        return stack[-1]
