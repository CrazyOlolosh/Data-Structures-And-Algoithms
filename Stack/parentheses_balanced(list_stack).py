class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list) - 1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()


def is_balanced_parentheses(parentheses):
    stack = Stack()
    for p in parentheses:
        if p == '(':
            stack.push(p)
        else:
            if stack.is_empty():
                return False
            else:
                stack.pop()
    return stack.is_empty()


balanced_parentheses = '((()))'
unbalanced_parentheses = '((())))'

print(is_balanced_parentheses(balanced_parentheses))

print(is_balanced_parentheses(unbalanced_parentheses))


"""
    EXPECTED OUTPUT:
    ----------------
    True
    False

"""
