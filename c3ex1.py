arr = [x.split() for x in input("Enter Input : ").split(",")]
class Stack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def __str__(self):
        s = 'stack of '+ str(self.size())+' items : '
        for ele in self.items:
            s += str(ele)+' '
        return s
    def push(self, i):
        self.items.append(i)

    def pop(self):   #edit code
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

s = Stack()
isfirst = True
i = 0
for ele in arr:
    if(ele[0]=="A"):
        s.push(ele[1])
        print("Add = "+ele[1]+" and Size = " + str(s.size()))
    elif(ele[0]=="P"):
        if(s.size()!=0):
            print("Pop = " + s.pop() + " and Index = " + str(s.size()))
        else:
            print("-1")
print("Value in Stack = ",end="")
if(s.size()!=0):
    ans = []
    for i in range(s.size()):
        ans.append(s.pop())
    ans.reverse()
    for ele in ans:
        print(ele,end=" ")
else:
    print("Empty",end="")
    