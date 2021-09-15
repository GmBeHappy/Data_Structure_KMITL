from collections import deque
class Queue:
    def __init__(self, q = None):
      if q == None:
        self.items = deque()
      else:
        self.items = deque(q,len(q))
    def __str__(self):
        if (self.isEmpty()):
          return "Empty"
        s = ''
        for ele in self.items:
          s += str(ele)+' '
        return s
    def enQueue(self, i):
      self.items.append(i)

    def deQueue(self):
      return self.items.popleft()

    def isEmpty(self):
      return len(self.items) == 0

    def size(self):
      return len(self.items)

p, t = input('Enter people and time : ').split()
t = int(t)
q1, q2, q3 = Queue(), Queue(), Queue()
for i in p : 
    q1.enQueue(i)
t1 = t2 = 0
for i in range(1, t + 1) :
    if t1 % 3 == 0 and not q2.isEmpty():
        q2.deQueue()
        t1 = 0
    if t2 % 2 == 0 and not q3.isEmpty() :
        q3.deQueue()
        t2 = 0

    if q2.size() < 5 and not q1.isEmpty(): 
        q2.enQueue(q1.deQueue())
    elif q3.size() < 5 and not q1.isEmpty(): 
        q3.enQueue(q1.deQueue())
    if not q2.isEmpty() : 
        t1 += 1
    if not q3.isEmpty() : 
        t2 += 1
    print(f'{i} {list(q1.items)} {list(q2.items)} {list(q3.items)}')