from Node import Node

class Queue:
    """This class creates queue.

    Class methods:
    pushBack(value) this method creates a new object based on the Node() class
    with the given value and adds it to the end of the queue
    
    pop() this method returns the first element of the queue and removes it

    isEmpty() this methods returns False if the queue is empty
    """
    def __init__(self):
        self.queue = Node()
        self.endQueue = self.queue
    
    def pushBack(self, value):
        if self.endQueue.value == None:
            self.endQueue.value = value
            return
        newNode = Node(value=value)
        self.endQueue.next = newNode
        newNode.last = self.endQueue
        self.endQueue = newNode
        return
    
    def pop(self):
        if self.isEmpty():
            return None
        popVal = self.queue.value
        if self.queue.next == None:
            self.queue.value = None
            return popVal
        self.queue = self.queue.next
        self.queue.last = None
        return popVal
    
    def isEmpty(self):
        return self.endQueue is self.queue and self.queue.value == None
