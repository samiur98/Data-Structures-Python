class Node:
    #Node Class that is used in the implementation of the AVL Tree.

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None #The LeftChild of the Node.
        self.right = None #The RightChild of the Node.
        self.parent = None #The parent of the Node.
        self.height = 0 #The height of the node is the maximum level of the node from the root node of the tree.( No of edges taken to get to the node from the root node in the tree)

    def __str__(self):
        return "Node"

class AVLTree:
    #An Implementation of the AVL Binary Search Tree Data Structure.

    def __init__(self):
        self.root = None
    def __str__(self):
        return "AVL-Tree"

    def is_empty(self):
        #Method that returns True if the Tree is empty, false otherwise.
        if self.root == None:
            return True
        else:
            return False

    def get_height(self, node):
        #Returns the height of a node in a tree.
        #The height of a node is the largest path of the node to a leaf node.
        #A leaf node is a node with no children
        if node == None:
            return -1
        else:
            return (max(self.get_height(node.left), self.get_height(node.right))) + 1

    def is_balanced(self, node):
        #Returns True if the node is balanced, False otherwise.
        #A node is balanced if the difference between the left and right subtree of the node is no greater than 1 and no less than -1.
        balance_factor = self.get_height(node.left)-self.get_height(node.right)
        if balance_factor > 1:
            return False
        elif balance_factor < -1:
            return False
        else:
            return True

    def search(self, key):
        #Method that searches for an element in the tree, given the key of the element.
        #If the element exists, the value is returned, None is returned otherwise.
        temp = self.root
        while temp != None:
            if temp.key == key:
                return temp.value
            elif temp.key > key:
                temp = temp.left
            else:
                temp = temp.right

        return None

    def insert(self,key, value):
        #Method that inserts a key/value pair into the Tree.
        #Returns True if successfull insertion occurs, False otherwise.
        #Failure to insert occurs when a key/value pair that already exists is attempted to be inserted again.
        if self.search(key) != None:
            return False
        else:
            new_node = Node(key, value)
            node = self.root
            if node == None:
                self.root = new_node
                return True
            while(True):
                if node.key > key:
                    if node.left == None:
                        node.left = new_node
                        new_node.parent = node
                        break
                    else:
                        node = node.left
                else:
                    if node.right == None:
                        node.right = new_node
                        new_node.parent = node
                        break
                    else:
                        node = node.right
            if self.is_balanced(self.root) == False:
                self.balance_tree()
            return True

    def left_rotate(self,node):
        #Helper function for balance_tree method.
        parent = node.parent
        left = node.left
        if parent == self.root:
            self.root = node
        parent.right = None
        node.left = parent
        node.parent = parent.parent
        if parent.parent != None:
            if node.parent.right == parent:
               node.parent.right = node
            else:
                node.parent.left = node
        parent.parent = node
        parent.right = left

    def right_rotate(self, node):
        #Helper function for the balance_tree method.
        parent = node.parent
        right = node.right
        if parent == self.root:
            self.root = node
        parent.left = None
        node.right = parent
        node.parent = parent.parent
        if parent.parent != None:
            if node.parent.left == parent:
               node.parent.left = node
            else:
                node.parent.right = node
        parent.parent = node
        parent.left = right

    def balance_tree(self):
        #Method that restores AVL property of tree.
        node = self.root
        is_left = False
        while(self.is_balanced(node) == False):
            if(self.get_height(node.left) > self.get_height(node.right)):
                is_left = True
                node = node.left
            else:
                is_left = False
                node = node.right
        if is_left:
            if self.get_height(node.right) < self.get_height(node.left):
                self.right_rotate(node)
            else:
                self.left_rotate(node.right)
                self.right_rotate(node.parent)
        else:
            if self.get_height(node.left) < self.get_height(node.right):
                self.left_rotate(node)
            else:
                self.right_rotate(node.left)
                self.left_rotate(node.parent)

    def delete(self, key):
        #Method that deletes a key/value pair from the Search Tree.
        #Returns True upon successfull deletion.
        #Returns False if key/value pair does not exist.
        node = self.root
        while(node != None):
            if node.key == key:
                break
            elif node.key > key:
                node = node.left
            else:
                node = node.right
        if node == None:
            #Case where Key/Value pair is not present in the BST.
            return False
        if (node.left == None) and (node.right == None):
            #Case where Node has no children
            if self.root == node:
                self.root = None
                return True
            if node.parent.right == node:
                node.parent.right = None
            else:
                node.parent.left = None
            node.parent = None
            return True
        elif (node.left == None) and (node.right != None):
            #Case where node has right child only.
            if self.root == node:
                self.root=node.right
                return True
            if node.parent.right == node:
                node.parent.right = node.right
            else:
                node.parent.left = node.right
            node.parent = None
            return True
        elif (node.left != None) and (node.right == None):
            #Case where node has left child only.
            if self.root == node:
                self.root = node.left
                return True
            if node.parent.right == node:
                node.parent.right = node.left
            else:
                node.parent.left = node.left
            node.parent = None
            return True
        else:
            #Case where node has two children.
            minimum = self.findMin(node.right)
            node.key = minimum[0]
            node.value = minimum[1]
            return True

    def findMin(self, node):
        #Helper function to be used in the delete method.
        #Removes the minimum node in a subtree and returns a tuple containing the key and value of the node. (In that order.)
        while node.left != None:
            node = node.left
        key = node.key
        value = node.value
        self.delete(key)
        return (key, value)
