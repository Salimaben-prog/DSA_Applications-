class Deque:
    def __init__(self):
        self.items=[]
    def add_in_rear(self,item):
        self.items.insert(0,item)
    def remove_from_rear(self):
        return self.items.pop(0)
    def add_in_front(self,item):
        self.items.append(item)
    def remove_from_front(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
def palindrome(s):
    d=Deque()
    for ch in s :
        d.add_in_rear(ch)
    while d.size()>1:
        left= d.remove_from_rear()
        right=d.remove_from_front()
        if left!=right:
            return False
    return True

print(palindrome('toot'))
