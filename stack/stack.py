# pylint: disable=no-member
"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        
        return self.size

    def push(self, value):
        self.value = value
        self.size += 1
        
        return self.storage.insert(0, self.value)

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.pop(0)

""" 
stack = Stack()
print(f"list: {stack.storage}")
print(f"Length of the stack: {len(stack)}")
print(f"we add the value to 2 to the stack")
print(f"list: {stack.storage}")
stack.push(2)
print(f"we add the value to 5 to the stack")
stack.push(5)
print(f"list: {stack.storage}")
print(f"we add the value to 7 to the stack")
stack.push(7)
print(f"list: {stack.storage}")
print(f"Length of the stack: {len(stack)}")
print(f"Size: {stack.size}")
print(f"we pop to the stack")
stack.pop()
print(f"list: {stack.storage}")
print(f"Length of the stack: {len(stack)}")
print(f"Size: {stack.size}")
stack.pop()
print(f"list: {stack.storage}")
print(f"Length of the stack: {len(stack)}")
print(f"Size: {stack.size}")
stack.pop()
print(f"list: {stack.storage}")
print(f"Length of the stack: {len(stack)}")
print(f"Size: {stack.size}")
 """
