class Node:
    
    #Node class that is to be used with the following implementation of Linked Lists.
    def __init__(self,value):
        self.value = value #Variable that holds the data represented by the node.
        self.next = None #Pointer to the next element in the linked list
        self.prev = None #Pointer to the previous element in the linked list(Used only in the case of Doubly Linked List)

    def __str__(self):
        return "Node"

class SinglyLinkedList:

    #An implementation of the Singly Linked List Data Structure.
    def __init__(self):
        self.head = None #The head or starting point of the list

    def __str__(self):
        return "SinglyLinkedList"

    def is_empty(self):
        #Method that returns true if Linked List is empty, false otherwise.
        if(self.head == None):
            return True
        else:
            return False

    def search(self,value):
        #Method that searches for a value within the Linked List
        #Returns true if found, false otherwise
        temp = self.head
        while(temp != None):
            if(temp.value == value):
                return True
            temp = temp.next
        return False

    def add(self,value):
        #Method that adds an element to the Linked List.
        node = Node(value)
        temp = self.head
        if(self.is_empty()):
            self.head = node
        else:
            while(temp.next != None):
                temp = temp.next
            temp.next = node

    def delete(self,value):
        #Method that deletes a value in the Linked List.
        #Returns True if the delete was successful,False otherwise.
        if(self.is_empty() == False):
            if(self.head.value == value):
                self.head = self.head.next
                return True
            node_1 = self.head
            node_2 = self.head.next
            if(node_2 == None):
                return False
            while(node_2 != None):
                if(node_2.value == value):
                    node_1.next = node_2.next
                    return True
                node_1 = node_2
                node_2 = node_2.next
        return False

class DoublyLinkedList():

    #An implementation of the Doubly Linked List Data Structure.
    def __init__(self):
        self.head = None #The head or the starting point of the Linked List.

    def __str__(self):
        return "DoublyLinkedList"

    def is_empty(self):
        #Method that checks whether the linked list is empty or not.
        #Returns True if the linked list is empty, false otherwise.
        if(self.head == None):
            return True
        else:
            return False

    def search(self,value):
        #Method that searches for a value in the linked list.
        #Returns True if the value is found,false otherwise
        temp = self.head
        while(temp != None):
            if (temp.value == value):
                return True
            temp = temp.next
        return False

    def add(self,value):
        #Method that adds a node, representing the value to the end of the linked list.
        node = Node(value)
        if(self.is_empty()):
            self.head = node
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = node
            node.prev = temp

    def delete(self,value):
        #Method that deletes a value from the Linked List.
        #Returns True if the delete was successful, false otherwise.
        if(self.is_empty()):
            return False
        if(self.head.value == value):
            self.head = self.head.next
            if(self.head != None):
                self.head.prev = None
            return True
        node_1 = self.head
        node_2 = self.head.next
        if(node_2 == None):
            return False
        while(node_2 != None):
            if(node_2.value == value):
                next = node_2.next
                if(next != None):
                    next.prev = node_1
                node_1.next = next
                node_2.next = None
                node_2.prev = None
                return True
            node_1 = node_2
            node_2 = node_2.next
        return False


