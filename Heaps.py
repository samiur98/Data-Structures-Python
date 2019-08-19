class MinHeap:
    #An implementation of the Min Heap Data Structure.

    def __init__(self):
        self.size = 0 #Variable that keeps track of the number of elements in the list.
        self.elements = [None] #List where the elements of the heap are to be stored.

    def __str__(self):
        return "MinHeap"

    def is_empty(self):
        #Method that checks whether the list is empty or not.
        #Returns True if heap is empty, false otherwise.
        if(self.size == 0):
            return True
        else:
            return False

    def percUp(self,i):
        #Method that percolates an entry in the heap up.
        #Intended to be a helper function to the insert method.
        while i//2 > 0:
            if(self.elements[i//2] > self.elements[i]):
                self.elements[i//2], self.elements[i] = self.elements[i], self.elements[i//2]
            else:
                break
            i = i//2

    def insert(self,element):
        #Method that inserts an element into the heap.
        self.elements.append(element)
        self.size = self.size + 1
        self.percUp(self.size)

    def percDown(self,i):
        #Method that percolates an entry in the heap down.
        #Intended to be a helper function to delMin method.
        while i * 2 <= self.size:
            min_child = i * 2
            if (i * 2) + 1 <= self.size:
                if self.elements[i * 2] > self.elements[(i * 2) + 1]:
                    min_child = (i * 2) + 1
            if self.elements[i] > self.elements[min_child]:
                self.elements[i], self.elements[min_child] = self.elements[min_child], self.elements[i]
            else:
                break
            i = min_child

    def delMin(self):
        #Method that returns the minimum value in the heap.
        #Restores Heap property afterwards.
        #Returns None if Heap is empty
        if self.size == 0:
            return None
        else:
            value = self.elements[1]
            self.elements[1], self.elements[self.size] = self.elements[self.size], self.elements[1]
            self.elements.pop()
            self.size = self.size - 1
            self.percDown(1)
            return value
