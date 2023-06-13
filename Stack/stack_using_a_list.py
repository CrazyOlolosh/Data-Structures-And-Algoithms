class Stack:
    def __init__(self, value=None):
        if value is None:
            self.items = []
        else:
            self.items = [value]

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.items == []:
            return None
        else:
            return self.items.pop()
