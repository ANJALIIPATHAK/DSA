class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if(char == "+"):
                res = stack.pop() + stack.pop()
                stack.append(res)
            elif(char == "-"):
                a = stack.pop()
                b = stack.pop()
                res = b - a
                stack.append(res)
            elif(char == "*"):
                res = stack.pop() * stack.pop()
                stack.append(res)
            elif(char == "/"):
                a = stack.pop()
                b = stack.pop()
                res = int(b / a)
                stack.append(res)
            else:
                stack.append(int(char))
        return stack[0]
            
