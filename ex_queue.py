class Queue:
    def __init__(self):
        self.items=[]
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def is_empty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items)
def hot_potato(name_list,num):
    q=Queue()
    for name in name_list:
        q.enqueue(name)
    while q.size()>1:
        for i in range(num):
             q.enqueue(q.dequeue())
        q.dequeue()
    return q.dequeue()

num=2
name_list=['salima','rachid','hanane']
print(hot_potato(name_list,num))
