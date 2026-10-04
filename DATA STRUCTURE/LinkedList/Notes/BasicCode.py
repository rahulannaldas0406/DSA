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

'''def twopointer(head):
    slow=head
    fast=head

    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next

    return slow '''

'''class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def PalidromeLL(head):
    slow=head
    fast=head

    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next

    second=slow.next

    prev=None

    while second:
        next_node=second.next
        second.next=prev
        prev=second
        second=next_node

    first=head
    second=prev

    while second:
        if first.val!=second.val:
            return False
        first=first.next
        second=second.next

    return True

def build_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head

head = build_list([1, 2, 2, 1])
print(PalidromeLL(head))  # True

# Test: 1 -> 2 -> 3 (not a palindrome)
head = build_list([1, 2, 3])
print(PalidromeLL(head))  # False'''

'''class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oddEven(head):
    odd=head
    even=head.next
    even_node=even

    while even and even.next:
        odd.next=even.next
        odd=odd.next

        even.next=odd.next
        even=even.next

    odd.next=even_node

    return head


def build_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head

def print_list(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print(vals)

# head = build_list([1, 2, 2, 1])
# oddEven(head)  # True
# print(head)
# # Test: 1 -> 2 -> 3 (not a palindrome)
# head = build_list([1, 2, 3])
# oddEven(head)
# print(head)


head = build_list([1, 2, 3, 4, 5])
oddEven(head)
print_list(head)  # [1, 3, 5, 2, 4]

head = build_list([2, 4, 6, 8])
oddEven(head)
print_list(head)  # [2, 6, 4, 8]

head = build_list([1])
oddEven(head)
print_list(head)  # [1]

head = build_list([])
oddEven(head)
print_list(head)  # []
'''




