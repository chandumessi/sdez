def insert_pos(self,data):
    new_node=Node(data)
    temp=self.head
    for i in range(1,pos-1):
        temp=temp.next
    new_node.previous=temp
    new_node.next