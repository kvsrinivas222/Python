#Stack Implementation using Linked List

class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

class Stack:
    def __init__(self):
        self.top=None

    def push(self,ele):
        new_none=Node(ele)
        if self.top is None:
            self.top=new_none
        else:
            new_none.next=self.top
            self.top=new_none

    def pop(self):
        if self.top==None:
            print("Stack is Undeflow")
        else:
            print(self.top.data," popped from stack")
            self.top=self.top.next

    def peek(self):
        if self.top==None:
            print("Stack is Empty")
        else:
            print(self.top.data," is top of stack")

st=Stack()

while True:
    print("\n1.Push 2.Pop 3.Peek")
    ch=int(input("Enter Choice: "))
    if ch==1:
        ele=int(input("Enter Element to be push: "))
        st.push(ele)
    elif ch==2:
        st.pop()
    elif ch==3:
        st.peek()
