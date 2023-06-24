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
        temp.next=ne
        ne.prev=temp
        ne.next=None
    def insert_at_mid(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        np.next=temp.next
        temp.next=np
        np.prev=temp
        temp.next.prev=np
    def del_at_beg(self):
        temp=self.head
        self.head=temp.next
        temp.next.prev=None
    def del_at_end(self):
        prev1=self.head
        temp=self.head.next
        while temp.next!=None:
            temp=temp.next
            prev1=prev1.next
        prev1.next=None
    def del_at_mid(self,pos):
        t1=self.head
        temp=self.head.next
        for i in range(1,pos-1):
            temp=temp.next
            t1=temp.next
        t1.next=temp.next
        temp.next.prev=t1
        temp.prev=None
        t1.next.prev=None
        
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
print(n4.data)
D.display()
D.insert_at_beg(40)
D.display()
D.insert_at_end(50)
D.display()
D.insert_at_mid(2,60)
D.display()
D.del_at_beg()
D.display()
D.del_at_end()
D.display()
D.del_at_mid(2)
D.display()
