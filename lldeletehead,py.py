def delete_begaining(Self):
    temp=self.head
    self.head=temp.next
    temp.next=None
    
def delete_end(self):
    prev=self.head
    temp=self.head.next
    while temp.text is not None:
        temp=temp.next
        prev=prev.next
    prev.next= None
    
def delete_pos(Self):
    prev=self.head
    temp=self.head.next
    for i in range(1,pos-1):
        temp=temp.next
        prev=prev.next
    prev.next=temp.next