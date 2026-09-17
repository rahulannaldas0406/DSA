'''class Node:
    def __init__(self,data):
        self.data=data 
        self.next=None

node1=Node(10)
node2=Node(20)
node3=Node(30)
node5=Node(50)

node1.next=node2
node2.next=node3
node3.next=node5

#Inserting an node in middle part

node4=Node(40)
node3.next=node4
node4.next=node5

#Deletion of a node 
node3.next=node5

head=node1

current=head

while current:
    print(current.data)
    current=current.next'''

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
f=Node(5)

a.next=b
b.next=c
c.next=d
d.next=f


#Counting number of node in linked list or checking length

'''def count_nodes(head):
    current=head
    count=0

    while current:
        count+=1
        current=current.next
    return count
ans=count_nodes(a)
print(ans)'''

#searching a node in list

'''def search_node(head,num):
    current=head

    while current:
        if current.data==num:
            return True
        current=current.next
    return False
ans=search_node(a,9)
print(ans)'''

'''head=a

def reverse(head):
    prev=None
    current=head

    while current:
        next_node=current.next
        current.next=prev
        prev=current
        current=next_node
        

    return prev

head=reverse(head)

current=head
while current:
    print(current.data)
    current=current.next'''





#Two pointer in linked list

def twopointer(head):
    slow=head
    fast=head

    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next

    return slow 
