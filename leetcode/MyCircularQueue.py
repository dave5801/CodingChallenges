class MyCircularQueue:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.size = k
        self.queue = []
        self.items = 0
        

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.items == self.size:
            return False
        else:
            self.queue.append(value)
            self.items += 1
            return True
        

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.queue:
            self.queue.pop(0)
            self.items -= 1
            return True
        return False
        

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.items > 0:
            return self.queue[0]
        return -1
        

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.items > 0:
            return self.queue[-1]
        return -1
        

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        if self.items == 0:
            return True
        else:
            return False
        

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        if self.items == self.size:
            return True
        else:
            return False
        

if __name__ == '__main__':
    circularQueue = MyCircularQueue(8)
    
    a = circularQueue.enQueue(7) 
    b = circularQueue.deQueue()
    c = circularQueue.Front()  
    d = circularQueue.deQueue()
    e = circularQueue.Front()
    f = circularQueue.Rear()
    g = circularQueue.enQueue(0) 
    h = circularQueue.isFull()
    i = circularQueue.deQueue()
    j = circularQueue.Rear()
    k = circularQueue.enQueue(3)

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)
    print(h)
    print(i)
    print(j)
    print(k)


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
'''
["MyCircularQueue","enQueue","deQueue","Front","deQueue","Front","Rear","enQueue","isFull","deQueue","Rear","enQueue"]
[[3],[7],[],[],[],[],[],[0],[],[],[],[3]]
'''