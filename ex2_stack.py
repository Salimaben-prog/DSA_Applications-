class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def is_empty(self):
        return len(self.items)==0
    def pop_item(self):
        if not self.is_empty():
            return self.items.pop()
        return None

def check_balanced(my_str):
    s=Stack()
    for i in my_str:
        if i in '[{(':
            s.push(i)
        else:
            if  s.is_empty():
                return False
            else:
                if not check_matching(s.pop_item(),i):
                    return False
    return s.is_empty()

def check_matching(l,r):
    all_l='[{('
    all_r=']})'
    return all_l.index(l)==all_r.index(r)


s = "{({([][])}())}"
print(f'This "{s}" balanced or not?')
print(check_balanced(s))
