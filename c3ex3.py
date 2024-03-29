class Stack:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def __str__(self):
        s = 'stack of ' + str(self.size())+' items : '
        for ele in self.items:
            s += str(ele)+' '
        return s

    def push(self, i):
        self.items.append(i)

    def pop(self):  # edit code
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


def postFixeval(ss):
    s = Stack()
    for ele in ss:
        if ele.lstrip('-').isdigit():
            s.push(int(ele))
        else:
            ele1 = s.pop()
            ele2 = s.pop()
            result = 0
            if ele == '+':
                result = ele1 + ele2
            elif ele == '*':
                result = ele1 * ele2
            elif ele == '/':
                result = ele2 / ele1
            elif ele == '-':
                result = ele2 - ele1
            s.push(result)
    return s.pop()

print(" ***Postfix expression calcuation***")
token = list(input("Enter Postfix expression : ").split())
print("Answer : ",'{:.2f}'.format(postFixeval(token)))