class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def is_empty(self):
        return len(self.items)==0
    def reverse_items(self):
        return self.items.reverse()
    def pop_items(self):
        return self.items.pop()

def decimal_To_Binary(n):
    s=Stack()
    while n >0 :
        rem= n%2
        s.push(rem)
        n//=2
    bin_string=""
    while not s.is_empty():
        bin_string+=str(s.pop_items())
    return bin_string

n=213
res=decimal_To_Binary(n)
print(res)
