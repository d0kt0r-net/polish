""" Polish calculator object-oriented code """


class PolishExpression:
    _expression: list

    def __init__(self, expression: str):
        valid_signs = '+-*/().'
        pre_sign_char = '+-*/('
        sign_char = '+-'
        operator_precedence = {
            '(': 0,
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
        }

        filtered_string = ''.join(filter(lambda c: c.isdigit() or c in valid_signs, expression))
        expression_list = list()
        prev_char = '('
        i = 0

        while i < len(filtered_string):
            cur_char = filtered_string[i]
            if prev_char in pre_sign_char and cur_char in sign_char or cur_char.replace('.', '0').isdigit():
                j = 1
                while i + j < len(filtered_string) and filtered_string[i + j].replace('.', '0').isdigit():
                    j += 1
                expression_list.append(float(filtered_string[i: i + j]))
                i += j
            else:
                expression_list.append(cur_char)
                i += 1
            prev_char = filtered_string[i - 1]

        self._expression = list()
        plain_stack = list()

        for element in expression_list:
            if isinstance(element, str):
                if element == ')':
                    stack_element = plain_stack.pop()
                    while stack_element != '(':
                        self._expression.append(stack_element)
                        stack_element = plain_stack.pop()
                else:
                    if element != '(':
                        while plain_stack and operator_precedence[plain_stack[-1]] >= operator_precedence[element]:
                            stack_element = plain_stack.pop()
                            self._expression.append(stack_element)

                    plain_stack.append(element)
            else:
                self._expression.append(element)

        while plain_stack:
            stack_element = plain_stack.pop()
            self._expression.append(stack_element)

    def __iter__(self):
        for element in self._expression:
            yield element

    def __str__(self):
        return str(self._expression)


class Stack:
    _stack: list

    def __init__(self):
        self._stack = list()

    def push(self, element):
        self._stack.append(element)

    def pop(self):
        element = self._stack.pop()
        return element


class PolishCalculator:
    _expression: PolishExpression

    def __init__(self, expression: PolishExpression):
        self._expression = expression

    def process(self) -> float:

        stack = Stack()
        for element in self._expression:
            if isinstance(element, str):  # operators
                second_argument = stack.pop()
                first_argument = stack.pop()
                if element == '+':
                    operation_result = first_argument + second_argument
                elif element == '-':
                    operation_result = first_argument - second_argument
                elif element == '*':
                    operation_result = first_argument * second_argument
                elif element == '/':
                    operation_result = first_argument / second_argument
                else:
                    raise KeyError
                stack.push(operation_result)
            else:
                stack.push(element)
        return stack.pop()


if __name__ == '__main__':
    while True:
        try:

            input_string = input()
            polish_expression = PolishExpression(input_string)
            calculator = PolishCalculator(polish_expression)
            result = calculator.process()

            print('---')
            print(input_string)
            print(polish_expression)
            print(result)

        except EOFError:
            break
