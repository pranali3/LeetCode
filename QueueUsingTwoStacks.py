class Queue:
    def __init__(self):
        self.instack = []
        self.outstack = []

    def enqueue(self, element):
        self.instack.append(element)

    def dequeue(self):
        # if empty
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()


if __name__ == "__main__":
    q = Queue()
    for i in range(10):
        q.enqueue(i)
        print("enqueue")
        print(q.instack)
        print(q.outstack)

    for i in range(10):
        q.dequeue()
        print("dequeue")
        print(q.instack)
        print(q.outstack)
