class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        for element in tokens:
            print(stack)
            if element == "+":
                stack.append(stack.pop()+stack.pop())
            elif element == "-":
                second_element = stack.pop()
                first_element = stack.pop()
                stack.append(first_element-second_element)
            elif element == "/":
                second_element = stack.pop()
                first_element = stack.pop()
                stack.append(int(first_element/second_element))
            elif element == "*":
                stack.append(stack.pop()*stack.pop())
            else:
                stack.append(int(element))
        print(stack)
        return stack[-1]
    