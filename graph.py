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

    def add(self,value,parentValue):
        current = self.__preorder_search(self.root,parentValue)#use pre-order search to get the parent node
        #print current.key
        if current.left_child == None:
        	current.left_child = node(None,None,current,value)#find if the node already has a left child
        	return current.left_child.key
        elif current.right_child == None:
        	current.right_child = node(None,None,current,value)#find if the node already has a right child
        	return
        else:
        	print ("Parent has two children, node not added")
   
    def Print(self):#print the whole tree 
    	self.print_preorder(self.root)

    def __preorder_search(self,current,goal):#search the tree recursively
        if current != None:
            if current.key == goal: 
                print "found",current.key
            	return current
            else:
        	    self.__preorder_search(current.left_child,goal)
        	    self.__preorder_search(current.right_child,goal)

    def delete(self,value):#pre-order
        current = self.preorder_search(self.root,value)
        if current == None:
            print("Node not found.")
        #if the node has two children 
        if current.left_child != None and current.right_child != None:
            print("Node not deleted, has two children")
        #if the node has no child
        if current.left_child == None and current.right_child == None:
            if current.parent.left_child == current.key:#if current node is the left child of its parent node
                current.parent.left_child = None
            else:#if current node is the right child of its parent node
                current.parent.right_child = None
            return
        #if the node has only one child
        print("Node not deleted, has one child")
        #try two delete the node that has only one child
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
 
    
t = Binary_tree(1)
print t.add(2,1)
print t.add(3,1)
t.Print()
t.add(4,2)
t.add(5,2)
t.Print()


#                1
#             2     3
#          4    5