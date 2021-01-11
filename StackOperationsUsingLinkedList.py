#Write a program to implement stack using linked list
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev=None
        
class Linklist:
    def __init__(self):
        self.head = None
        
    def push(self, node):
        node.next=self.head
        if self.head is not None:
            self.head.prev=node
        self.head=node
        
    def pop(self):
        if self.head is None: 
            return
        if self.head.next==None:
            self.head=None
        else:
            self.head=self.head.next
            self.head.prev=None
            
    def dispList(self):
        tmp = self.head
        while tmp:
            print(tmp.val)
            tmp = tmp.next

if __name__ == "__main__":
    ls=Linklist()
    step=True
    while step:
        op=input("enter operation:")
        if op=="1":
            ls.push(Node(input("enter element:")))
        elif op=="2":
            ls.pop()
        elif op=="3":
            ls.dispList()
        else:
            step=False

"""
output:
enter 1.push   2.pop   3.print   4.exit
enter operation:1
enter element:34
enter 1.push   2.pop   3.print   4.exit
enter operation:1
enter element:56
enter 1.push   2.pop   3.print   4.exit
enter operation:1
enter element:87
enter 1.push   2.pop   3.print   4.exit
enter operation:2
enter 1.push   2.pop   3.print   4.exit
enter operation:3
56
34
enter 1.push   2.pop   3.print   4.exit
enter operation:4
>>> """