from Node import Node

class Deque:
    """This class creates Deque.

    Class methods:
    pushBack(value) this method creates a new object based on the Node() class
    with the given value and adds it to the end of the deque

    pushFront(value) this method creates a new object based on the Node() class
    with the given value and adds it to the start of the deque

    popBack() this method returns the end element of the deque and removes it

    popFront() this method returns the first element of the deque and removes it

    isEmpty() this methods returns False if the deque is empty
    """
    def __init__(self):
        self.doubleQueue = Node()
        self.backQueue = self.doubleQueue
        self.frontQueue = self.doubleQueue        
        
    def pushBack(self, value):
        if self.backQueue.value == None:
            self.backQueue.value = value
            return
        newNode = Node(value= value)
        self.backQueue.last = newNode
        newNode.next = self.backQueue
        self.backQueue = newNode
        return
    
    def pushFront(self, value):
        if self.frontQueue.value == None:
            self.frontQueue.value = value
            return
        newNode = Node(value)
        self.frontQueue.next = newNode
        newNode.last = self.frontQueue
        self.frontQueue = newNode
        return
    
    def popBack(self):
        if self.isEmpty():
            return None
        retValue = self.backQueue.value 
        self.backQueue = self.backQueue.next
        self.backQueue.last = None
        return retValue
    
    def popFront(self):
        if self.isEmpty():
            return None
        retValue = self.frontQueue.value 
        self.frontQueue = self.frontQueue.last
        self.frontQueue.next = None
        return retValue
    
    def isEmpty(self):
        return self.backQueue is self.frontQueue
    

    


