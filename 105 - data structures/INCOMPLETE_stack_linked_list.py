# linked lists are... a lot

# for this, i'm gonna go ahead and steal a basic stack and explain each function
# in this example, the Stack class is made up of a bunch of nodes
# each of those nodes have a value
# and each of the nodes point to each other

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class Stack:
    def __init__(self):
        self.head = Node("head") # "head" is interchangable with "root"
        self.size = 0
    
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("The stack is empty")
        remove = self.head.next
        self.size -= 1
        return remove.value
    
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-2]

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0


if __name__ == "__main__":
    stack = Stack()
    for i in range (1, 11):
        stack.push(i)
    print(f"Stack: {stack}")