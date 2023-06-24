class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
class DLL:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while(temp):
                if temp.next!=None:
                    print(temp.data,end="-->")
                else:
                    print(temp.data,end="")
                    print()
                temp=temp.next
    def insert_at_beg(self,data):
        nb=Node(data)
        temp=self.head
        nb.next=temp
        temp.prev=nb
        self.head=nb
    def insert_at_end(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        ne.next=temp
        temp.next=ne
        ne.next=None
    def insert_at_mid(self,pos,data):
        nm=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        nm.prev=temp
        nm.next=temp.next
        temp.next=nm.prev
        temp.next=nm
    def del_at_beg(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    def del_at_end(self):
        t1=self.head
        temp=self.head.next
        while temp.next!=None:
            temp=temp.next
            t1=t1.next
        temp.prev=None
        t1.next=None
    def del_at_mid(self,pos):
        t1=self.head
        temp=self.head.next
        for i in range(1,pos-1):
            temp=temp.next
            t1=t1.next
        t1.next=temp.next
        temp.next=None
D=DLL()
n1=Node(10)
D.head=n1
n2=Node(20)
D.head.next=n2
n1.next=n2
n2.prev=n1
n3=Node(30)
n2.next=n3
n3.prev=n2
n4=Node(40)
print(n1.data)
print(n1.prev)
print(n2.data)
print(n2.prev)
print(n3.data)
print(n3.prev)
print(n4.data)
print(n4.prev)
D.display()
D.insert_at_beg(40)
D.display()
D.insert_at_end(50)
D.display()
D.insert_at_mid(2,5)
D.display()
D.del_at_beg()
D.display()
D.del_at_end()
D.display()
D.del_at_mid(3)
D.display()






