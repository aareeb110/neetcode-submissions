class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}

        for token in tokens:
            if token in operators:
                operand2 = stack.pop()
                operand1 = stack.pop()

                if token == "+":
                    result = operand1 + operand2
                elif token == "-":
                    result = operand1 - operand2
                elif token == "*":
                    result = operand1 * operand2
                elif token == "/":
                    result = int(operand1 / operand2)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack[0]