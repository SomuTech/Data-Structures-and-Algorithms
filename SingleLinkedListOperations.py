#SingleLinkedList
class Node:
    def __init__(self, val,name):
        self.val = val
        self.name = name
        self.next = None
        
class Linklist:
    def __init__(self):
        self.head = None
        self.last=None
        
    def inserthead(self, node):
        if self.head is None:
            self.head = node
            self.head.next=None
            
    def insertlast(self, node):
        if self.head.next is None:
            self.last=node
            self.head.next=self.last
            
    def insertlist(self, node):
        temp=self.head
        while temp:
            if temp.next==self.last:
                temp.next=node
                node.next=self.last
            temp=temp.next
            
    def delete(self, node):
        head =self.head
        if(val==self.head.val):
            self.head=self.head.next
        else:
            while(val!=head.next.val and head.next!=None):
                head=head.next
            if(head.next.val==val):
                prev=head
                head=head.next
                prev.next=head.next
                
    def recursion(self,head):
        if head!=None:
            self.recursion(head.next)
            print(head.val,head.name)
                
    def countlist(self):
        c=0
        tem=self.head
        while tem:
            c=c+1
            tem=tem.next
        print(c)
        
    def sortlist(self):
        current=self.head
        index=None
        while current !=None:
            index=current.next
            while(index !=None):
                if(current.name>index.name):
                    temp,temp1=current.name,current.val
                    current.name,current.val=index.name,index.val
                    index.name,index.val=temp,temp1
                index=index.next
            current=current.next
                
    def dispList(self):
        tmp = self.head
        while tmp:
            print("Roll Number:%s\tName:%s"%(str(tmp.val),str(tmp.name)))
            tmp = tmp.next

if __name__ == "__main__":
    sll = Linklist()
    print("{:20s}{}".format(" ","PRERANA READERS CLUB"))
    val,name=input("enter IdNumber and name of head:").split(" ")
    sll.inserthead(Node(val,name.upper()))
    val,name=input("enter IdNumber and name of in-charge:").split(" ")
    sll.insertlast(Node(val,name.upper()))
    print("enter:\n1.insert\n2.delete\n3.total members\n
	4.reverse list\n5.sort list\n6.display list")
    step=True
    while step:
        op=input("enter operation:")
        if op=='1':
            val,name=input("enter IdNumber and name of student:").split(" ")
            sll.insertlist(Node(val,name.upper()))
        elif op=='2':
            val,name=input("enter IdNumber and name:").split(" ")
            sll.delete(Node(val,name.upper()))
            print("list after deleting:")
            sll.dispList()
        elif op=='3':
            print("members count:",end=" ")
            sll.countlist()
        elif op=='4':
            print("list after reverse")
            sll.recursion(sll.head)
        elif op=='5':
            sll.sortlist()
            sll.dispList()
        elif op=='6':
            sll.dispList()
        else:
            step=False
		
"""
output:
enter IdNumber and name of head:1 boss
enter IdNumber and name of in-charge:7 incharge
enter:
1.insert
2.delete
3.total members
4.reverse list
5.sort list
6.display list
enter operation:1
enter IdNumber and name of student:2 nani
enter operation:1
enter IdNumber and name of student:3 madhu
enter operation:1
enter IdNumber and name of student:4 raghu
enter operation:2
enter IdNumber and name:3 madhu
list after deleting:
Roll Number:1	Name:BOSS
Roll Number:2	Name:NANI
Roll Number:4	Name:RAGHU
Roll Number:7	Name:INCHARGE
enter operation:3
members count: 4
enter operation:4
list after reverse
7 INCHARGE
4 RAGHU
2 NANI
1 BOSS
enter operation:5
Roll Number:1	Name:BOSS
Roll Number:7	Name:INCHARGE
Roll Number:2	Name:NANI
Roll Number:4	Name:RAGHU
enter operation:6
Roll Number:1	Name:BOSS
Roll Number:7	Name:INCHARGE
Roll Number:2	Name:NANI
Roll Number:4	Name:RAGHU
enter operation:h
>>> """