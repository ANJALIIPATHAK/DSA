class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        stack = []
        num = 0
        operator = "+"

        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)
            if (not char.isdigit() or i == len(s) - 1):
                if operator == "+":
                    stack.append(num)
                elif operator == "-":
                    stack.append(-num)
                elif operator == "*":
                    prev = stack.pop()
                    stack.append(prev * num)
                else:
                    prev = stack.pop()
                    stack.append(int(prev / num))
                num = 0
                operator = char
        return sum(stack)