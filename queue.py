#QUEUE
import types
import Queue
class Queue_int(object):
	
    def _init_(self,max=8):
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
    def isInteger(self,obj):
        return type(obj) == type(1)
    
    def isEmpty(self):
    	if self.queue.empty():
    		return True
    	else:
    	    return False


aaa = Queue_int()
aaa.queue = Queue.Queue(maxsize=max)
aaa.enqueue(1)
aaa.enqueue(2)
print aaa.dequeue()
print aaa.dequeue()
