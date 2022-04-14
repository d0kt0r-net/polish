""" Polish calculator functional code """
import operator
from structured import filter_data, prepare_polish


def prepare_functional_expression(input_expression: list) -> tuple:

    stack = list()
    for element in input_expression:
        if isinstance(element, str):  # operators
            second_argument = stack.pop()
            first_argument = stack.pop()
            if element == '+':
                operation = (operator.add, (first_argument, second_argument))
            elif element == '-':
                operation = (operator.sub, (first_argument, second_argument))
            elif element == '*':
                operation = (operator.mul, (first_argument, second_argument))
            elif element == '/':
                operation = (operator.truediv, (first_argument, second_argument))
            else:
                raise KeyError
            stack.append(operation)
        else:
            stack.append(element)
    return stack.pop()


def count_functional(expression):
    return expression[0].__call__(
        *map(count_functional, expression[1])
    ) if isinstance(expression, tuple) else expression


if __name__ == '__main__':
    while True:
        try:

            input_string = input()
            input_data = filter_data(input_string)
            polish_expression = prepare_polish(input_data)
            functional_expression = prepare_functional_expression(polish_expression)
            result = count_functional(functional_expression)

            print('---')
            print(input_string)
            print(polish_expression)
            print(result)

        except EOFError:
            break
