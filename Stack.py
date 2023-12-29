from Node import Node

class Stack:
    """This class creates stack.

    Class methods:
    push(value) this method creates a new object based on the Node() class
    with the given value and adds it to the end of the stack
    
    pop() this method returns an element from the end of the stack and removes it

    isEmpty() this methods returns False if the stack is empty
    """
    def __init__(self):
        self.stack = Node()
        self.endStack = self.stack

    def push(self, v):
        if self.endStack.value == None:
            self.endStack.value = v
            return
        newEndNode = Node(v)
        self.endStack.next = newEndNode
        newEndNode.last = self.endStack
        self.endStack = newEndNode
        return
    
    def pop(self):
        if self.isEmpty():
            return None
        if self.stack is self.endStack:
            return self.stack.value
        popVal = self.endStack.value
        self.endStack = self.endStack.last
        self.endStack.next = None
        return popVal
    
    def isEmpty(self):
        return self.endStack == None and self.stack.value == None