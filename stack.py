#STACK
import types

class Stack(object):
	
    def _init_(self):
        self.stack = []

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


aaa = Stack()
aaa.stack = []
aaa.push(1)
aaa.push(2)
print aaa.pop()
print aaa.pop()