from class_stek import Stack

BALANCED_BRACKETS = '[([])((([[[]]])))]{()}'
UNBALANCED_BRACKETS = '{{[(])]}}'


def check_ballance(str_):

    stack = Stack()
    for bracket in str_:
        if bracket in '([{':
            stack.push(bracket)
        else:
            if not stack.stack_list:
                return 'Несбалансированно'
            else:
                open_bracket = stack.pop()

                if open_bracket + bracket in ['()', '[]', '{}']:
                    continue
                else:
                    return 'Несбалансированно'

    return 'Сбалансированно'


if __name__ == '__main__':
    print(check_ballance(BALANCED_BRACKETS))
    print(check_ballance(UNBALANCED_BRACKETS))

