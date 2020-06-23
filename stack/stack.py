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
# Using a list
# class Stack:
#
#     def __init__(self):
#         self.size = 0
#         self.storage = []
#
#     def __len__(self):
#
#         return self.size
#
#     def push(self, value):
#         self.value = value
#         self.size += 1
#
#         return self.storage.insert(0, self.value)
#
#     def pop(self):
#         if self.size > 0:
#             self.size -= 1
#             return self.storage.pop(0)


# stack = Stack()
# print(f"list: {stack.storage}")
# print(f"Length of the stack: {len(stack)}")
# print(f"we add the value to 2 to the stack")
# print(f"list: {stack.storage}")
# stack.push(2)
# print(f"we add the value to 5 to the stack")
# stack.push(5)
# print(f"list: {stack.storage}")
# print(f"we add the value to 7 to the stack")
# stack.push(7)
# print(f"list: {stack.storage}")
# print(f"Length of the stack: {len(stack)}")
# print(f"Size: {stack.size}")
# print(f"we pop to the stack")
# stack.pop()
# print(f"list: {stack.storage}")
# print(f"Length of the stack: {len(stack)}")
# print(f"Size: {stack.size}")
# stack.pop()
# print(f"list: {stack.storage}")
# print(f"Length of the stack: {len(stack)}")
# print(f"Size: {stack.size}")
# stack.pop()
# print(f"list: {stack.storage}")
# print(f"Length of the stack: {len(stack)}")
# print(f"Size: {stack.size}")
#

# Using linked lists


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


class Stack(LinkedList):

    def __init__(self):

        self.size = 0
        self.storage = LinkedList()
        self.head = self.storage.head
        self.tail = self.storage.tail
        self.next = None



    def __len__(self):

        return self.size

    def push(self, value):
        self.value = value


        # new_node = Node(self.value)
        # new_node.next = self.head
        # self.head = new_node



        # create a node to add
        new_node = Node(value)
        # check if list is empty
        if self.head is None and self.tail is None:
          self.head = new_node
          self.tail = new_node

        else:
          # new_node should point to current head
          new_node.next = self.head
          # move head to new node
          self.head = new_node

        self.size += 1



    def pop(self):

        # # edge case - empty linked list
        # if self.head == None:
        #     return
        #
        # # Store head node
        # temp = self.head
        #
        # # If head needs to be removed
        # self.head = temp.next
        # temp = None
        #self.size -= 1

        # if list is empty, do nothing
        if not self.head:
          return None
        # if list only has one element, set head and tail to None
        if self.head.next is None:
          head_value = self.head.value
          self.head = None
          self.tail = None
          self.size -= 1
          return head_value
        # otherwise we have more elements in the list
        else:
            head_value = self.head.value
            self.head = self.head.next
            self.size = self.size - 1

            return head_value







#
#
#
# stack = Stack()
#
# print([node.value for node in stack])
# print(f"Length of the stack: {len(stack)}")
# print(f"we add the value to 2 to the stack")
#
# stack.push(2)
# print([node.value for node in stack])
# print(f"we add the value to 5 to the stack")
# stack.push(5)
# print([node.value for node in stack])
# print(f"we add the value to 7 to the stack")
# stack.push(7)
# print([node.value for node in stack])
# print(f"Length of the stack: {len(stack)}")
# print(f"Size: {stack.size}")
# print(f"we pop to the stack")
# stack.pop()
# print([node.value for node in stack])
# print(f"Length of the stack: {len(stack)}")
# print(f"Size: {stack.size}")
# print(f"we pop to the stack")
# stack.pop()
# print([node.value for node in stack])
# print(f"Length of the stack: {len(stack)}")
# print(f"Size: {stack.size}")
# print(f"we pop to the stack")
# stack.pop()
# print(f"Length of the stack: {len(stack)}")
# print([node.value for node in stack])
# print(f"Length of the stack: {len(stack)}")
# print(f"Size: {stack.size}")
