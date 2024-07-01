class MyCircularQueue:

    def __init__(self, k: int):
        self.cursize = 0
        self.size = k
        self.q = []

    def enQueue(self, value: int) -> bool:
        if self.cursize < self.size:
            self.cursize += 1
            self.q.append(value)
            return True
        return False

    def deQueue(self) -> bool:
        b = []
        print(self.q)
        if self.cursize > 0:
            self.cursize -= 1
            for i in range(len(self.q)-1):
                b.append(self.q.pop())
            self.q.pop()
            for i in range(len(b)):
                self.q.append(b.pop())
            return True
            print(self.q)
        return False

    def Front(self) -> int:
        if self.q:
            return self.q[0]
        return -1

    def Rear(self) -> int:
        if self.q:
            return self.q[self.cursize - 1]
        return -1

    def isEmpty(self) -> bool:
        return self.cursize == 0

    def isFull(self) -> bool:
        return self.cursize == self.size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
