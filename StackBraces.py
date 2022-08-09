class Stack:
    def __init__(self):
        self.init_stack = []

    def isEmpty(self):
        if not self.init_stack:
            return True
        else:
            return False

    def push(self, element):
        self.init_stack.append(element)

    def pop(self):
        return self.init_stack.pop()

    def peek(self):
        return self.init_stack[0]

    def size(self):
        return len(self.init_stack)


def braces_checker(braces):
    stack_verifier = True
    no_braces_verifier = True
    for elem in braces:
        if elem in '({[':
            braces_stack.push(elem)
            no_braces_verifier = False
        elif elem in ')}]':
            no_braces_verifier = False
            if braces_stack.size() == 0:
                stack_verifier = False
                break

            breaker = braces_stack.pop()
            if breaker == '(' and elem == ')':
                continue
            if breaker == '[' and elem == ']':
                continue
            if breaker == '{' and elem == '}':
                continue
            stack_verifier = False
            break
    if stack_verifier and braces_stack.size() == 0 and not no_braces_verifier:
        print('Сбалансированно')
    elif no_braces_verifier:
        print('Нет скобок')
    else:
        print('Несбалансированно')


if __name__ == '__main__':
    braces_stack = Stack()
    braces_string = input('Введите последовательность скобок:')
    braces_checker(braces_string)

