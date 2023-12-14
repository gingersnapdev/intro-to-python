# to understand what a linked list is
# we have to go over what a node is
# a node is an object

class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

# a node object has 2 properties
# val - the value that's assigned to it
# next - points to the next node
# when we write the constructor for the node
# set the value of next to None (null)
# because it doesnt point to anything (at least it doesnt yet)

# got it?
# node has 2 things: its own value, something to point to the next node in the list
# "what list?"
# this list fuckhead

class LinkedList:
    def __init__(self):
        self.head = None

# this object is called LinkedList, it's basically going to be a list
# at the start of every data structure (trees, linked lists, etc)
# you're going to have an object called "head" (or root) (when i spent 4 years learning java in school they always called it root)
# when writing the constructor for the LinkedList object
# we set the head of the list to None, since... well, it doesnt have a head
# not yet anyways
# let's initialize a new LinkedList

list1 = LinkedList()

# list1 is our new LinkedList
# let's make a new node

n = Node(1)

# n has a val of 1 -> print(n.val) returns 1
# n has doesnt point to anything -> print(n.next) returns None
# let's make n the new head of list1

list1.head = n

# let's create some new nodes

n2 = Node(2)
n3 = Node(3)

# now let's link the new nodes to n (in order)

list1.head.next = n2
n2.next = n3

# now they're linked
# it looks something like
# 1 -> 2 -> 3
# the -> represent the next property of the Node object