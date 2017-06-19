'''
implement a Queue data structure
'''

class Queue:

    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return data

    def peek(self):
        return self.queue[0]

    def sizeQueue(self):
        return len(self.queue)

    def getValues(self):
        return self.queue

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
print(q.sizeQueue())

print("dequeue: " + str(q.dequeue()))
print("dequeue: " + str(q.dequeue()))

print(q.sizeQueue())
print(q.getValues())

