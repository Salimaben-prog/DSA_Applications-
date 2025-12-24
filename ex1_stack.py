class Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def push(self,item):
        self.items.append(item)
    def peek(self):
        return self.items[-1]
    def pop_item(self):
        return self.items.pop()

def checked_balance(my_str):
    s=Stack()
    for i in my_str:
        if i == '(':
            s.push(i)
        else:
            if s.is_empty():
                return False
            else:
                s.pop_item()
    return s.is_empty()

s = "((())"
print(f'This "{s}" balanced or not?')
print(checked_balance(s))
