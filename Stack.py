class Stack:
    #An implementation of the Stack Data Structure.

    def __init__(self,limit):
        self.limit = limit #The capacity of the Stack, ie maximum number of elements.
        self.size = 0 #Variable that keeps track of the number of elements in the Stack.
        self.elements = [None] * limit #A list representing the stack is initilized and filled to maximum capacity with None objects.

    def __str__(self):
        return "Stack"

    def is_empty(self):
        #Method that checks whether the stack is empty or not.Returns True if empty, False otherwise.
        if (self.size == 0):
            return True
        else:
            return False

    def is_full(self):
        #Method that checks whether the stack is full or not.Returns True if full, False otherwise.
        if(self.size == self.limit):
            return True
        else:
            return False

    def peek(self):
        #Method that return the element on top of the stack, ie the element last added.
        #Returns None if Stack is empty.
        if (self.is_empty() == False):
            value = self.size - 1
            return self.elements[value]
        else:
            return None

    def push(self,element):
        #Method that pushes(adds) a new element onto the Stack.
        #Prints error message and returns None if Stack is full.
        if (self.is_full()):
            print("Stack Full!")
            return None
        else:
            value = self.size
            self.size = self.size + 1
            self.elements[value] = element

    def pop(self):
        #Method that pops(removes) and returns the element on top of the Stack.
        #Prints error message and returns None if Stack is empty.
        if(self.is_empty()):
            print("Stack Empty!")
            return None
        else:
            value = self.elements[self.size-1]
            self.elements[self.size-1] = None
            self.size = self.size - 1
            return value

