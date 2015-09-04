import types
import Queue

#QUEUE
class Queue_int(object):
	
    def __init__(self,max=100):
        self.queue = Queue.Queue(maxsize=max)

    def enqueue(self,obj):
    	if self.isInteger(obj):
            self.queue.put(obj)
        else:
        	raise Exception("Error: is not integer")

    def dequeue(self):
        if self.isEmpty():
        	raise Exception("Error: Queue is empty")
        else:
        	return self.queue.get()
            #get() del first obj and return it
    def isInteger(self,obj):#check if the number is integer
        return type(obj) == type(1)
    
    def isEmpty(self):
    	if self.queue.empty():
    		return True
    	else:
    	    return False

#STACK
class Stack(object):
    
    def __init__(self):
        self.stack = []#use list to store

    def push(self,obj):
        if self.isInteger(obj):
            self.stack.append(obj)
        else:
            raise Exception("Error: is not integer")

    def pop(self):
        if self.isEmpty():
            raise Exception("Error: Stack is empty")
        else:
            return self.stack.pop()

    def isInteger(self,obj):
        return type(obj) == type(1)
    
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

#BINARYTREE
class node:

    def __init__(self,right_child,left_child,parent,key):#constructor
        self.right_child = right_child
        self.left_child = left_child
        self.parent = parent
        self.key = key 


class Binary_tree:

    def __init__(self,root_key):
        self.root = node(None,None,None,root_key)
        self.search_result = node(None,None,None,None)

    def add(self,value,parentValue):
        self.__preorder_search(self.root,parentValue)#use pre-order search to get the parent node
        if self.search_result.key == parentValue:
            current = self.search_result
            #print current.key
            if current.left_child == None:
                current.left_child = node(None,None,current,value)#find if the node already has a left child
                return 
            elif current.right_child == None:
                current.right_child = node(None,None,current,value)#find if the node already has a right child
                return
            else:
                print ("Parent has two children, node not added")
        else:
            print("Parent not found")
        
   
    def Print(self):#print the whole tree 
        self.print_preorder(self.root)

    def __preorder_search(self,current,goal):#search the tree recursively
        if current != None:
            if current.key == goal: 
                #print "found",current.key
                self.search_result = current
            else:
                self.__preorder_search(current.left_child,goal)
                self.__preorder_search(current.right_child,goal)

    def delete(self,value):#pre-order
        self.__preorder_search(self.root,value)
        if self.search_result.key == value:
            current = self.search_result
            #if the node has two children 
            if current.left_child != None and current.right_child != None:
                print("Node not deleted, has two children")
                return
            #if the node has no child
            if current.left_child == None and current.right_child == None:
                if current.parent.left_child == current.key:#if current node is the left child of its parent node
                    current.parent.left_child = None
                    print("Node deleted")
                else:#if current node is the right child of its parent node
                    current.parent.right_child = None
                    print("Node deleted")
                return
            #if the node has only one child
            print("Node not deleted, has one child")
        else:
            print("Node not found.")
            #try to delete the node that has only one child
            '''if current.left_child == None:
                if current.parent.left_child.key == current.key:#the node is the left child of its parent node
                    current.right_child.parent = current.parent
                    current.parent.left_child = current.right_child
                else:#the node is the right child of its parent node
                    current.right_child.parent = current.parent
                    current.parent.right_child = current.right_child
                else:# current.right_child == None:
                if current.parent.left_child.key == current.key:#the node is the left child of its parent node
                    current.left_child.parent = current.parent
                    current.parent.left_child = current.left_child
                else:#the node is the right child of its parent node
                    current.left_child.parent = current.parent
                    current.parent.right_child = current.left_child
            return''' 
    def print_preorder(self,current):#pre-order traversal & print the tree
        if current == None:
            return None
        print(current.key)
        self.print_preorder(current.left_child)
        self.print_preorder(current.right_child)

#GRAPH
import types

class graph:

    def __init__(self,graphDict = {}):
        self.gra = graphDict

    def addVertex(self,value):
        if self.gra.has_key(value):
            print ('Vertex already exists')
        else:
            self.gra[value] = []
    def printVertex(self):
        print self.gra
    def addEdges(self,value1,value2):
        if self.gra.has_key(value1) and self.gra.has_key(value2):
            self.gra[value1].append(value2)
            self.gra[value2].append(value1)
        else:
            print("One or more vertices not found")
    def findVertex(self,value):
        if self.gra.has_key(value):
            print self.gra[value]
        else:
            print("Vertex not found")

i = 0
#test queue
q = Queue_int()
print("Queue Test:")
while i < 11:
    #print i
    q.enqueue(i)
    i += 1
while q.isEmpty() == False:
    print q.dequeue()
print("**********")

i = 0
#test stack
s = Stack()
print("Stack Test:")
while i < 11:
    s.push(i)
    i += 1
while s.isEmpty() == False:
    print s.pop()
print("**********")

#test Binary tree
print("Binary tree Test")
t = Binary_tree(1)
t.add(2,1)
t.add(3,1)
t.add(4,2)
t.add(5,2)
t.add(6,3)
t.add(7,3)
t.add(8,4)
t.add(9,4)
t.add(10,6)
t.add(11,6)
t.Print()
t.delete(8)
t.delete(10)
t.delete(1)
t.Print()
#                  1
#              2      3
#           4    5  6   7
#         8  9    10 11
print("**********")
#test graph
i = 0
j = 0
g = graph()
print("Graph test")
while i < 11:
    g.addVertex(i)
    i += 1
g.printVertex()
while i >= 0:
    g.addEdges(1,i)
    i -= 1
while i < 11:
    g.addEdges(0,i)
    i += 1
g.printVertex()
i = 0
while i < 6:
    g.findVertex(i)
    i += 1
print("**********")