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

arr = [ele.split(' ') for ele in input("Enter Input : ").split(',')]
q = Queue()
i=0
for ele in arr:
  if ele[0] == 'E':
    q.enQueue(ele[1])
    print(f"Add {ele[1]} index is {i}")
    i += 1
  elif ele[0] == 'D':
    if q.isEmpty():
      print(-1)
      continue
    print(f"Pop {q.deQueue()} size in queue is {q.size()}")
    i -= 1
if(q.isEmpty()):
    print("Empty")
else:
    ans = []
    for i in range(q.size()):
        ans.append(q.deQueue())
    print("Number in Queue is :  [", end="'")
    print(*ans, sep="', '", end="']")