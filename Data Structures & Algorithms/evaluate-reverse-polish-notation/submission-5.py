class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for character in tokens:
            print(stack)
            print(character)
            if character == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif character == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif character == "-":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b - a)
            elif character == "/":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(int(float(b) / a))

            else:
                stack.append(character)
        
        print(stack)
        return stack[0]