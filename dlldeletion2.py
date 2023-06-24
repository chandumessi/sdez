def delete_begin(self):
    temp=self.head
    self.head=temp.next
    temp.next.previous=None
    temp.next=None
    
def delete_end(self):
    prev=self.head
    temp=self.head.next
    while temp.next is not None:
        temp=temp.next
        prev=prev.next
    prev.next=None
    temp.previous= None
    
def insert_pos(self,data):
    new_node=Node(data)
    temp=self.head
    for i in range(1,pos-1):
        temp=temp.next
    new_node.previous=temp
    new_node.next