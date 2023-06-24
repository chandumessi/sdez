n=int(input("enter the size of the stack"))
stc=[]
def push_element():
    if len(stc)==n:
        print("stack is full")
    else:
        element=input("enter element for stack to insert")
        stc.append(element)
        print(stc)
def pop_element():
    if not stc:
        print("stack is empty,add elements")
    else:
        e = stc.pop()
        print(e,"removed")
        print(stc)
while True:
    print("select operation 1.push 2.pop 3.quit.")
    choice=int (input())
    if choice==1:
        push_element()
    elif choice==2:
        pop_element()
    elif choice==3:
        break
    else:
        print("enter correct operation")