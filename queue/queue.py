"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order.

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Queue?

Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

# Using a list
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
#
#     def __len__(self):
#         return self.size
#
#     def enqueue(self, value):
#         self.value = value
#         self.size += 1
#
#         return self.storage.insert(0, self.value)
#
#     def dequeue(self):
#         if self.size > 0:
#             self.size -= 1
#             return self.storage.pop(-1)
#
#




# queue = Queue()
#
# print(queue.storage)
# print(f"Length of the queue: {len(queue)}")
# print(f"we add the value to 2 to the queue")
#
# queue.enqueue(2)
# print(queue.storage)
# print(f"we add the value to 5 to the queue")
# queue.enqueue(5)
# print(queue.storage)
# print(f"we add the value to 7 to the queue")
# queue.enqueue(7)
# print(queue.storage)
# print(f"Length of the queue: {len(queue)}")
# print(f"Size: {queue.size}")
# print(f"we dequeue the queue")
# queue.dequeue()
# print(queue.storage)
# print(f"Length of the queue: {len(queue)}")
# print(f"Size: {queue.size}")
# print(f"we dequeue the queue")
# queue.dequeue()
# print(queue.storage)
# print(f"Length of the queue: {len(queue)}")
# print(f"Size: {queue.size}")
# print(f"we dequeue the queue")
# queue.dequeue()
# print(queue.storage)
# print(f"Length of the queue: {len(queue)}")
# print(f"Size: {queue.size}")



# Using a linked list
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


class Queue(LinkedList):

    def __init__(self):

        self.size = 0
        self.storage = LinkedList()
        self.head = self.storage.head
        self.tail = self.storage.tail
        self.next = None



    def __len__(self):

        return self.size

    def enqueue(self, value):
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
          self.tail.next = new_node
          # move head to new node
          self.tail = new_node

        self.size += 1



    def dequeue(self):


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

        else:
            # otherwise we have more elements in the list
            head_value = self.head.value
            self.head = self.head.next
            self.size -= 1
            return head_value
        self.size -= 1


#
# queue = Queue()
#
# print([node.value for node in queue])
# print(f"Length of the queue: {len(queue)}")
# print(f"we add the value to 2 to the queue")
#
# queue.enqueue(2)
# print([node.value for node in queue])
# print(f"we add the value to 5 to the queue")
# queue.enqueue(5)
# print([node.value for node in queue])
# print(f"we add the value to 7 to the queue")
# queue.enqueue(7)
# print([node.value for node in queue])
# print(f"Length of the queue: {len(queue)}")
# print(f"Size: {queue.size}")
# print(f"we dequeue the queue")
# queue.dequeue()
# print([node.value for node in queue])
# print(f"Length of the queue: {len(queue)}")
# print(f"Size: {queue.size}")
# print(f"we dequeue the queue")
# queue.dequeue()
# print([node.value for node in queue])
# print(f"Length of the queue: {len(queue)}")
# print(f"Size: {queue.size}")
# print(f"we dequeue the queue")
# queue.dequeue()
# print([node.value for node in queue])
# print(f"Length of the queue: {len(queue)}")
# print(f"Size: {queue.size}")
