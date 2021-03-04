class Node:
    def __init__(self,value):
        self.info= value
        self.link= None
    
class linkedlist:
    print("""            WELCOME TO OUR LINKED LIST PROJECT """)
    def __init__(self):
        self.start=None

    def traverse(self):
        if self.start is None:
            print("List is empty")
            return
        else:
            print("This list contains : ",end=" ")
            p = self.start
            while p is not None:
                print(p.info," ",end=" ")
                p=p.link
        print()
         
    def insert_beg(self,data):
        new_node = Node(data)
        new_node.link = self.start
        self.start= new_node

    def insert_end(self,data):
        new_node = Node(data)
        if self.start is None:
            self.start = new_node
            return
        p= self.start
        while p.link is not None:
            p=p.link
        p.link=new_node

    def delete_first(self):
        if self.start is None:
            return
        self.start=self.start.link

    def delete_last(self):
        if self.start is None:
            return
        if self.start.link is None:
            self.start= None
            return
        p=self.start
        while p.link.link is not None:
            p=p.link
        p.link=None


list=linkedlist()
print("Your list has been initiated")
while True:
    print("""
1 : Traverse
2 : Insert new node at the beginning
3 : Insert new node at the end
4 : Delete first node
5 : Delete last node
6 : Quit""")
    option=int(input("Enter your command :"))
    if option==1:
        list.traverse()
    elif option ==2:
        data=int(input("Enter the value to be inserted at the beginning : "))
        list.insert_beg(data)
        list.traverse()
    elif option ==3:
        data=int(input("Enter the value to be inserted at the end : "))
        list.insert_end(data)
        list.traverse()
    elif option ==4:
        list.delete_first()
        list.traverse()
    elif option ==5:
        list.delete_last()
        list.traverse()
    elif option ==6:
        break
    else:
        print("Wrong option")
    print()
