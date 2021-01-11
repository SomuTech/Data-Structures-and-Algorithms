#DublylinkedList
class Node: 
    def __init__(self,emp_id,emp_dept,emp_sal, emp_mobileno): 
        self.prev = None
        self.emp_id=emp_id
        self.emp_dept=emp_dept
        self.emp_sal=emp_sal
        self.emp_mobileno=emp_mobileno
        self.next = None
        
class doublyLinkedList: 
    def __init__(self): 
        self.head = None
        
    def begInsert(self, new_node): 
        new_node.next = self.head
        if self.head is not None: 
            self.head.prev = new_node
        self.head = new_node
        
    def endInsert(self, new_node): 
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
    
    def insert(self, prev_node, new_node):
        if prev_node is None: 
            return
        temp=self.head
        while temp.emp_id!=prev_node.emp_id:
            temp=temp.next
        new_node.next=temp.next
        temp.next=new_node
        new_node.prev=prev_node

    def deleteBeg(self):
        if self.head is None: 
            return
        if self.head.next==None:
            self.head=None
        else:
            self.head=self.head.next
            self.head.prev=None

    def delete(self,node):
        if self.head is None:
            return
        if self.head.emp_id==node.emp_id:
            self.head=None
        temp=self.head
        while temp.emp_id!=node.emp_id:
            temp=temp.next
        temp.prev.next=temp.next
        temp.next.prev=temp.prev
        
    def deleteEnd(self):
        if self.head==None:
            return
        if self.head.next==None:
            self.head=None
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp=temp.prev
        temp.next=None 
            
    def countlist(self):
        c=0
        tem=self.head
        while tem:
            c=c+1
            tem=tem.next
        print(c)
        
    def displayList(self, node): 
        while node is not None: 
            print("Employee Id:%d\nEmployee Dept:%s\nEmployee sal:%f\nEmployee
			Mobile.no:%s"%(int(node.emp_id),str(node.emp_dept),float(node.emp_sal),
			str(node.emp_mobileno)))
            last = node 
            node = node.next
          
if __name__ == "__main__":
    dls=doublyLinkedList()
    print("1=End insertion\n2=count\n3.1=insert end,3.2=delete end\n4.1=insert
	front,4.2=delete front\n5.1=insert,5.2=delete\nprint=to display\n6.exit")
    step=True
    while step:
        op=input("enter operation:")
        if op=="1":
            emp_id,emp_dept,emp_sal, emp_mobileno=input("id,dept,sal,mobileno :").split(" ")
            dls.endInsert(Node(emp_id,emp_dept,emp_sal, emp_mobileno))
        elif op=="2":
            dls.countlist()
        elif op=="3.1":
            emp_id,emp_dept,emp_sal, emp_mobileno=input("id,dept,sal,mobileno :").split(" ")
            dls.endInsert(Node(emp_id,emp_dept,emp_sal, emp_mobileno))
        elif op=="3.2":
            dls.deleteEnd()
        elif op=="4.1":
           emp_id,emp_dept,emp_sal, emp_mobileno=input("id,dept,sal,mobileno :").split(" ")
           dls.begInsert(Node(emp_id,emp_dept,emp_sal, emp_mobileno))
        elif op=="4.2":
            dls.deleteBeg()
        elif op=="5.1":
            pemp_id,pemp_dept,pemp_sal, pemp_mobileno=input("enter previous id,dept,sal,mobileno
			:").split(" ")
            emp_id,emp_dept,emp_sal, emp_mobileno=input("id,dept,sal,mobileno :").split(" ")
            dls.insert(Node(pemp_id,pemp_dept,pemp_sal, pemp_mobileno),
			Node(emp_id,emp_dept,emp_sal, emp_mobileno))
        elif op=="5.2":
            emp_id,emp_dept,emp_sal, emp_mobileno=input("id,dept,sal,mobileno :").split(" ")
            dls.delete(Node(emp_id,emp_dept,emp_sal, emp_mobileno))
        elif op=="print":
            dls.displayList(dls.head)
        else:
            step=False
    
"""output:
1=End insertion
2=count
3.1=insert end,3.2=delete end
4.1=insert front,4.2=delete front
5.1=insert,5.2=delete
print=to display
6.exit
enter operation:1
emp_id,emp_dept,emp_sal, emp_mobileno :12 cse 7354 35887
enter operation:1
emp_id,emp_dept,emp_sal, emp_mobileno :13 it 8475 728356
enter operation:2
2
enter operation:1
emp_id,emp_dept,emp_sal, emp_mobileno :14 csse 84763 893746
enter operation:3.2
enter operation:4.1
emp_id,emp_dept,emp_sal, emp_mobileno :10 me 4656 27356
enter operation:4.2
enter operation:5.1
enter previous emp_id,emp_dept,emp_sal, emp_mobileno :12 cse 7354 35887
emp_id,emp_dept,emp_sal, emp_mobileno :11 ops 36345 345875
enter operation:5.2
emp_id,emp_dept,emp_sal, emp_mobileno :13 it 8475 728356
enter operation:print
Employee Id:12
Employee Dept:cse
Employee sal:7354.000000
Employee Mobile.no:35887
Employee Id:11
Employee Dept:ops
Employee sal:36345.000000
Employee Mobile.no:345875
enter operation:6
"""
