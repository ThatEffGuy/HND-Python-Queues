#oop implementation of a queue
#the queue class

class Queue:
    def __init__(self):
        self.items = []
    def add(self, item):
        self.items.append(item)
    def delete(self):
        itemToDelete = self.items [0]
        del self.items [0]
        return itemToDelete
    def size(self):
        return len(self.items)
    def report(self):
        return self.items



myQueue = Queue()
myQueue. add("Glen")
myQueue. add("Stephen")
myQueue. add ("Jamie")
myQueue. add ("Luke")

print("The size of the queue is: ", myQueue.size())
print("The content of the queue is: ", myQueue.report())
print("We are going to delete an item from the queue: ", myQueue.delete())
print("The content of the queue after deletion: ", myQueue.report())
