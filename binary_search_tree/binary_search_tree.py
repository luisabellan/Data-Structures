"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    # Insert the given value into the tree
    def insert(self, value):
        # I'm here
        # take the current value of our node (self.value)
        # compare to the new value we want to insert



        # if new value < self.value
        # IF self.left is already taken by a node
        # make that (left) node, call insert
        # set the left to the new node with the new value

        if value < self.value:
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)

        # if new value >= self.value
        # IF self.right is already taken by a node
        # make that (right) node call insert
        # set the right child to the new node with new value
        elif value >= self.value:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)



    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        # compare the target to current value
        # if current value < target
        found = False
        if self.value < target:
            # check the left subtree (self.left.contains(target))
            # if you cannot go left, return False
            if self.left is None:
                return False
            found = self.left.contains(target)

        # if current value >= target
        if self.value >= target: #the equals sign is not needed here because the case "self.value == target" is already contemplated above
            # check if right subtree contains target
            # if you cannot go right, return False
            if self.right is None:
                return False
            found = self.right.contains(target)

        return found

    # Return the maximum value found in the tree
    def get_max(self): # it can be done iteratively or recursively

        # done recursively:

        # the largest value will always be to the right of the current node
        # if we can go right, lets find the largest number there by calling get_max on the right subtree
        # if we cannot go right, return the current value
        # Call the function `fn` on the value of each node

        if self.right is None:
            return self.value
        return self.right.get_max()



    def for_each(self, fn):

        # call function on the current value fn(self.value)
        fn(self.value)
        if self is None:
            self.for_each(fn)

        # if you can go left, call for_each on the left tree
        if self.left is not None:
            self.left.for_each(fn)

        # if you can go right, call for_each on the right tree
        if self.right is not None:
            self.right.for_each(fn)


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        #create a queue for nodes
        # add the first node to the queue
        # while queue is not empty
            # remove the first node from the queue
            # print the removed nodes
            # add all children into the queue
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # create a stack for nodes
        # add the first node to the stack
        # while the stack is not empty
            # get the current node from the top of the stack
            # print that node
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
