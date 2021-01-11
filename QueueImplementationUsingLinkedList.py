#Write a program to implement queue using linked list

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev=None
        
class Linklist:
    def __init__(self):
        self.head = None

    def EnQueue(self, new_node): 
        new_node.next = None
        if self.head is None: 
            new_node.prev = None
            self.head = new_node
            return
        last = self.head
        while(last.next is not None): 
            last = last.next
        last.next = new_node
        new_node.prev = last
        return

    def DeQueue(self):
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
            ls.EnQueue(Node(input("enter element:")))
        elif op=="2":
            ls.DeQueue()
        elif op=="3":
            ls.dispList()
        else:
            step=False

"""
output:
enter 1.enqueue   2.dequeue   3.print   4.exit
enter operation:1
enter element:45
enter 1.enqueue   2.dequeue   3.print   4.exit
enter operation:1
enter element:34
enter 1.enqueue   2.dequeue   3.print   4.exit
enter operation:1
enter element:67
enter 1.enqueue   2.dequeue   3.print   4.exit
enter operation:2
enter 1.enqueue   2.dequeue   3.print   4.exit
enter operation:3
34
67
enter 1.enqueue   2.dequeue   3.print   4.exit
enter operation:4
>>> """