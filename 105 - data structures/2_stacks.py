# we'll go over this in a bit
from collections import deque

# you can use a list as a stack
# what is a stack?
# think of a stack of sliced cheese
# you start the stack with 1 slice of cheese
# then add more on top of it
# eventually you want to eat cheese, so you eat the top piece, the newest piece
# stacks operate similar to that
# first in last out (FILO)

# you can use a regular list/array [] as a stack
stack = []

# .append(whatever) appends to the stack
stack.append('a')
stack.append('b')
stack.append('c')

# let's test
print(stack)
# ['a', 'b', 'c']

# taking a piece of cheese off the top of the stack of cheese
# that's done with .pop()
stack.pop()
print(stack)
# ['a', 'b']

# look at the import statement at the top
# from collections import deque
# collections is a library, we're gonna take deque from it
# you can also use deque to implement a stack
deque_stack = deque()

# .append() and .pop() are O(1) when using dequeue
# if you're using a list, those operations are O(n)
# they're written essentially the same though
deque_stack.append('a')
deque_stack.append('b')
deque_stack.append('c')
deque_stack.pop()
deque_stack.pop()
deque_stack.pop()

# some other stack functions are:
# .empty() - returns boolean on whether the stack is empty or not
# .size() - returns size of stack
# .top() & .peek() - returns the top element (does not remove it)
# .push(whatever) - inserts 'whatever' to the top of the stack