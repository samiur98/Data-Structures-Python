class Node:
    #Node class used in the following implementations of the Hash Table or Hash Map Data Structure.

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None #Only used for Separate Chaining implementation.
        self.flag = False #Only used for Open Addressing implementations.

    def __str__(self):
        return "Node"

    def get_hash(self):
        #A Hash Function, that assumes that the key is a string.
        value = 0
        for a in self.key:
            value = value + ord(a) * 31
        return value

    def set_flag(self):
        #A function that marks a node as deleted.
        #Used in the Open Addressing implementations.
        self.flag = True

class HashTable1:
    #The following is an implementation of the Hash Table or Hash Map Data Structure.
    #Linear probing(Open Addressing) is used for collision resolution.

    def __init__(self):
        self.size = 0 #Variable that keeps track of number of elements in the Hash Table.
        self.table = [Node(None, None)] * 10 #Table initialized with 10 slots

    def __str__(self):
        return "HashTable: Linear Probing Collision Resolution"

    def is_empty(self):
        #Method that checks whether the table is empty or not.
        #Returns True if the table is empty, False otherwise.
        if(self.size == 0):
            return True
        else:
            return False

    def load_factor(self):
        #Method that returns the load factor of the HasTable.
        size = float(self.size)
        capacity = float(len(self.table))
        return size/capacity

    def search(self, key):
        #Method that searches for a key in the HashTable
        #If key is found, corresponding value is returned, None is returned otherwise
        node = Node(key, None)
        hash_value = node.get_hash()
        slot = hash_value % len(self.table)
        while True:
            if(self.table[slot].key == key):
                return self.table[slot].value
            if(self.table[slot].key == None):
                if(self.table[slot].flag == False):
                    return None
            if(slot == (len(self.table)-1)):
                slot = 0
            else:
                slot = slot + 1

    def insert(self, key, value):
        #Method that inserts a key/value pair into the Hash Table.
        #If element with key/value pair exists, it is replaced by new entry.
        node = Node(key, value)
        slot = node.get_hash() % len(self.table)
        if(self.table[slot] == None):
            self.table[slot] = node
            self.size = self.size + 1
        else:
            while self.table[slot].key != None:
                if(self.table[slot].key == key):
                    break
                if(slot == (len(self.table)-1)):
                    slot = 0
                else:
                    slot = slot + 1
            self.table[slot] = node
            self.size = self.size + 1
        if(self.load_factor() >= 0.75):
            self.resize()

    def resize(self):
        #Method that resizes or extends the Hash Table, to avoid clustering.
        old_table = self.table
        self.table = [Node(None, None)] * (len(self.table) * 2)
        self.size = 0
        for element in old_table:
            if(element.key != None):
                self.insert(element.key, element.value)

    def delete(self,key):
        #Method that deletes key/value pairing in HashTable
        #Returns True in the case of successfull removal,False otherwise.
        node = Node(key, None)
        slot = node.get_hash() % len(self.table)
        new_node = Node(None, None)
        new_node.set_flag()
        while True:
            if(self.table[slot].key == key):
                self.table[slot] = new_node
                self.size = self.size - 1
                return True
            if(self.table[slot].key == None):
                if(self.table[slot].flag == False):
                    return False
            if(slot == (len(self.table)-1)):
                slot = 0
            else:
                slot = slot + 1

    def printTable(self):
        #Method that prints the table in a way that is easy to debug.
        list=[]
        for element in self.table:
            list.append((element.key, element.value))
        print list

class HashTable2:
    #The following is an implementation of the Hash Table or Hash Map Data Structure.
    #Quadratic probing(Open Addressing) is used for collision resolution.

    def __init__(self):
        self.size = 0 #Variable that keeps track of number of elements in the Hash Table.
        self.table = [Node(None, None)] * 10 #Table initialized with 10 slots

    def __str__(self):
        return "HashTable: Quadratic Probing Collision Resolution"

    def is_empty(self):
        #Method that checks whether the table is empty or not.
        #Returns True if the table is empty, False otherwise.
        if(self.size == 0):
            return True
        else:
            return False

    def load_factor(self):
        #Method that returns the load factor of the HasTable.
        size = float(self.size)
        capacity = float(len(self.table))
        load = size/capacity
        return load

    def search(self,key):
        #Method that searches for a key in the HashTable
        #If key is found, corresponding value is returned, None is returned otherwise
        node = Node(key, None)
        hash_value = node.get_hash()
        slot = hash_value%len(self.table)
        counter = 1
        trial = slot
        while True:
            if self.table[trial].key == key:
                return self.table[trial].value
            if self.table[trial].key == None:
                if self.table[trial].flag == False:
                    return None
            increment = counter * counter
            trial = slot + increment
            if trial >= len(self.table):
                trial = trial - len(self.table)
            counter = counter + 1

    def insert(self, key, value):
        #Method that inserts a key/value pair into the Hash Table.
        #If element with key/value pair exists, it is replaced by new entry.
        node = Node(key, value)
        slot = node.get_hash() % len(self.table)
        if self.table[slot] == None:
            self.table[slot] = node
            self.size = self.size + 1
        else:
            counter = 1
            trial = slot
            while self.table[trial].key != None:
                if self.table[trial].key == key:
                    break
                increment = counter * counter
                trial = slot + increment
                if trial >= len(self.table):
                    trial = trial - len(self.table)
                counter = counter + 1
            self.table[trial] = node
            self.size = self.size + 1
        if self.load_factor() >= 0.75:
            self.resize()

    def resize(self):
        #Method that resizes or extends the Hash Table, to avoid clustering.
        old_table = self.table
        self.table = [Node(None, None)] * (len(self.table) * 2)
        self.size = 0
        for element in old_table:
            if(element.key != None):
                self.insert(element.key, element.value)

    def delete(self,key):
        #Method that deletes key/value pairing in HashTable
        #Returns True in the case of successfull removal,False otherwise.
        node = Node(key, None)
        slot = node.get_hash() % len(self.table)
        new_node = Node(None,None)
        new_node.set_flag()
        counter = 1
        trial = slot
        while True:
            if self.table[trial].key == key:
                self.table[trial] = new_node
                self.size = self.size - 1
                return True
            if self.table[trial].key == None:
                if self.table[trial].flag == False:
                    return False
            increment = counter * counter
            trial = slot + increment
            if trial >= len(self.table):
                trial = trial - len(self.table)
            counter = counter + 1

    def printTable(self):
        #Method that prints the table in a way that is easy to debug.
        list = []
        for element in self.table:
            list.append((element.key, element.value))
        print list

class HashTable3:
    #The following is an implementation of the Hash Table or Hash Map Data Structure.
    #Separate Chaining is used for collision resolution.

    def __init__(self):
        self.size = 0 #Variable that keeps track of the number of elements in the table.
        self.table = [Node(None, None)] * 10 #List used to store Key/Value pair.

    def __str__(self):
        return "HashTable: Separate Chaining Collision Resolution"

    def is_empty(self):
        #Method that checks whether the table is empty or not. Returns True if table is empty, False otherwise.
        if self.size == 0:
            return True
        else:
            return False

    def search(self, key):
        #Method that searches for a Key/Value pair in the Hash Table.
        #Returns the corresponding value if found, None otherwise.
        node = Node(key, None)
        slot = node.get_hash() % len(self.table)
        temp = self.table[slot]
        while temp!= None:
            if temp.key == key:
                return temp.value
            temp = temp.next
        return None

    def insert(self, key, value):
        #Method that inserts a Key/Value pair into the Hash Table.
        node = Node(key, value)
        slot = node.get_hash() % len(self.table)
        temp = self.table[slot]
        if temp.key == None:
            self.table[slot] = node
            self.size = self.size + 1
        else:
            while temp.next != None:
                temp = temp.next
            temp.next = node
            self.size = self.size + 1

    def delete(self, key):
        #Method that deletes a Key/Value pair in the Hash Table.
        #Returns True if removal is successfull, False otherwise
        node = Node(key, None)
        slot = node.get_hash() % len(self.table)
        temp = self.table[slot]
        if temp.key == key:
            if temp.next == None:
                self.table[slot] = Node(None, None)
                self.size = self.size - 1
                return True
            else:
                self.table[slot] = temp.next
                self.size = self.size - 1
                return True
        while temp.next != None:
            if temp.next.key == key:
                if temp.next.next == None:
                    temp.next = None
                    self.size = self.size - 1
                    return True
                else:
                    temp.next = temp.next.next
                    self.size = self.size - 1
                    return True
            temp = temp.next
        return False

    def printTable(self):
        #A print table method for debugging
        list = []
        for node in self.table:
            list.append((node.key, node.value))
        print list
