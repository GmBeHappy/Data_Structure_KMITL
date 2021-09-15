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
        for i, ele in enumerate(self.items):
          if i != self.size()-1:
            s += repr(str(ele))+', '
          else:
            s += repr(str(ele))
        return s
    def enQueue(self, i):
      self.items.append(i)

    def deQueue(self):
      return self.items.popleft()

    def isEmpty(self):
      return len(self.items) == 0

    def size(self):
      return len(self.items)

def encodeMsg(word, key) :
    q1, q2, q3 = Queue(word), Queue(key), Queue()
    for i in range(q1.size()) :
        buff = q1.items[i]
        if('A' <= buff <= 'Z'): 
            buff = chr((ord(q1.items[i]) + q2.items[i] - 65) % 26 + 65)
        else: 
            buff = chr((ord(q1.items[i]) + q2.items[i] - 97) % 26 + 97)
        q3.enQueue(buff)
    return q3.items

def decodeMsg(wordEncode, key) :
    q1, q2, q3 = Queue(wordEncode), Queue(key), Queue()
    for i in range(q1.size()) :
        buff = q1.items[i]
        if('A' <= buff <= 'Z'): 
            buff = chr((ord(q1.items[i]) - q2.items[i] - 65) % 26 + 65)
        else: 
            buff = chr((ord(q1.items[i]) - q2.items[i] - 97) % 26 + 97)
        q3.enQueue(buff)
    return q3.items


s, n    = input('Enter String and Code : ').split(',')
q1, q2  = Queue(), Queue()
[q1.enQueue(i) for i in s if not i == ' '] 
[q2.enQueue(int(n[i % len(n)])) for i in range(q1.size()) if q2.size() < q1.size()]
print(f'Encode message is :  {list(encodeMsg(q1.items, q2.items))}')
print(f'Decode message is :  {list(decodeMsg(encodeMsg(q1.items, q2.items), q2.items))}')