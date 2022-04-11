""" Polish calculator structured code """


def filter_data(input_string: str) -> list:
    valid_signs = '+-*/()'

    pre_sign_char = '+-*/('
    sign_char = '+-'

    filtered_string = ''.join(filter(lambda c: c.replace('.', '').isdigit() or c in valid_signs, input_string))
    expression_list = list()
    prev_char = '('
    i = 0

    while i < len(filtered_string):
        cur_char = filtered_string[i]
        if prev_char in pre_sign_char and cur_char in sign_char or cur_char.replace('.', '').isdigit():
            j = 1
            while i + j < len(filtered_string) and filtered_string[i + j].replace('.', '').isdigit():
                j += 1
            expression_list.append(int(filtered_string[i: i + j]))
            i += j
            pass
        else:
            expression_list.append(cur_char)
            i += 1
        prev_char = cur_char

    return expression_list


def prepare_polish(expression_list: list) -> list:
    operator_precedence = {
        '(': 0,
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
    }

    result_expression = list()
    stack = list()

    for element in expression_list:
        if isinstance(element, str):
            if element == ')':
                stack_element = stack.pop()
                while stack_element != '(':
                    result_expression.append(stack_element)
                    stack_element = stack.pop()
            else:
                if element != '(':
                    while stack and operator_precedence[stack[-1]] >= operator_precedence[element]:
                        stack_element = stack.pop()
                        result_expression.append(stack_element)

                stack.append(element)
        else:
            result_expression.append(element)

    while stack:
        stack_element = stack.pop()
        result_expression.append(stack_element)

    return result_expression


def count_polish(input_expression: list) -> float:

    stack = list()
    for element in input_expression:
        if isinstance(element, str):  # operators
            first_argument = stack.pop()
            second_argument = stack.pop()
            if element == '+':
                operation_result = first_argument + second_argument
            if element == '-':
                operation_result = first_argument - second_argument
            if element == '*':
                operation_result = first_argument * second_argument
            if element == '/':
                operation_result = first_argument / second_argument
            stack.append(operation_result)
        else:
            stack.append(element)
    return stack.pop()


if __name__ == '__main__':
    while True:
        try:

            input_string = input()
            input_data = filter_data(input_string)
            polish_expression = prepare_polish(input_data)
            result = count_polish(polish_expression)

            print('---')
            print(input_string)
            print(polish_expression)
            print(result)

        except EOFError:
            break

