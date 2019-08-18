class Queue:
    #An implementation of the Queue Data Structure.

    def __init__(self,limit):
        self.limit = limit #The maximum capacity of the Queue.(Maximum number of elements)
        self.size = 0 #Variable that keeps track of the number of elements is the Queue.
        self.elements = [None] * limit #A list representing the Queue. It is initialized and filled with None objects.

    def __str__(self):
        return "Queue"

    def is_empty(self):
        #Method that checks whether the Queue is empty or not.Returns True if Queue is empty, false otherwise.
        if(self.size == 0):
            return True
        else:
            return False

    def is_full(self):
        #Method that checks whether the Queue is full or not.Returns True if Queue is full, false otherwise.
        if(self.size == self.limit):
            return True
        else:
            return False

    def peek(self):
        #Method that returns the element ahead in the queue.(The element that is to be removed next.)
        #Returns None if Queue is empty.
        if(self.is_empty()):
            return None
        else:
            return self.elements[0]

    def enqueue(self,element):
        #Method that adds an element to the queue.
        #Returns None and prints error message if Queue is full.
        if(self.is_full()):
            print("Queue Full!")
            return None
        else:
            self.elements[self.size] = element
            self.size = self.size + 1

    def dequeue(self):
        #Method that removes and returns the element that was added earliest in the queue.
        #Returns None if Queue if empty.
        if(self.is_empty()):
            print ("Queue Empty!")
            return None
        else:
            value = self.elements[0]
            for i in range(0, self.size - 1):
                self.elements[i] = self.elements[i + 1]
            self.size = self.size - 1
            self.elements[self.size] = None
            return value
