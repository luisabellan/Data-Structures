
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        # Stores a node, that corresponds to our first node in the list
        self.head = None
        # stores a node that is the end of the list
        self.tail = None
        # Stores its size
        self.size = 0

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # return all values in the list a -> b -> c -> d -> None

    def __str__(self):
        output = ''
        current_node = self.head  # create a tracker node variable
        while current_node is not None:  # loop until its NONE

            output += f'{current_node.value} -> '

            current_node = current_node.next  # update the tracker node to the next node

        return output

    def add_to_head(self, value):
        # create a node to add
        new_node = Node(value)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1

        else:
            # new_node should point to current head
            new_node.next = self.head
            # move head to new node
            self.head = new_node
            self.size += 1

    def add_to_tail(self, value):
        # create a node to add
        new_node = Node(value)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            # point the node at the current tail, to the new node
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1

    # remove the head and return its value
    def remove_head(self):
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
        head_value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return head_value

    def get_max(self):

        if not self.head:
            return None
        max_val = self.head.value
        current = self.head
        while current:
            if current.value > max_val:
                max_val = current.value
            current = current.next
        return max_val

    def contains(self, value):
        if self.head is None:
            return False

        # Loop through each node, until we see the value, or we cannot go further
        current_node = self.head

        while current_node is not None:
            # check if this is the node we are looking for
            if current_node.value == value:
                return True

            # otherwise, go to the next node
            current_node = current_node.next
        return False


# example
linked_list = LinkedList()

print("We add 100 to the tail")
linked_list.add_to_tail(100)
print(linked_list)
print(linked_list.get_max())

print("We add 55 to the tail")
linked_list.add_to_tail(55)
print(linked_list)
print(linked_list.get_max())

print("We add 101 to the tail")
linked_list.add_to_tail(101)
print(linked_list)
print(linked_list.get_max())
