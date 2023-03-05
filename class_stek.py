class Stack:
    def __init__(self):
        self.stack_list = []

    def is_empty(self):
        return self.stack_list == []

    def push(self, element):
        self.stack_list.insert(0, element)

    def pop(self):
        top_element = self.stack_list[0]
        del self.stack_list[0]
        return top_element

    def peek(self):
        return self.stack_list[0]

    def size(self):
        return len(self.stack_list)
