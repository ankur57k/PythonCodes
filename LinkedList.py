from Node import Node

class LinkedList(object):

    def __init__(self,head=None):
        self.head=head

    def insert(self,data):
        print "LinkedList::insert()"
        new_node=Node(data)
        new_node.set_next(self.head)
        self.head=new_node

    def size(self):
        print "LinkedList::size()"
        current=self.head
        count=0
        while current:
            count += 1
            current=current.get_next()
        return count

    def printll(self):
        print "LinkedList::printll()"
        current=self.head
        print "Values: "
        while current:
            print(current.get_data())
            current=current.get_next()

    def search(self,data):
        print "LinkedList::search()"
        current=self.head
        found=False
        while current and found is False:
            if current.get_data() == data:
                found=True
            else:
                current=current.get_next()
        if current is None:
            print "not in list"
            #raise ValueError("Data not in list")
        return current

    def delete(self,data):
        print "LinkedList::delete()"
        current=self.head
        found=False
        previous=None
        while current and found is False:
            if current.get_data() == data:
                found=True
            else:
                previous=current
                current=current.get_next()
        if current is None:
            print "not in list"
            #raise ValueError("Data not in list")
        if previous is None:
            self.head=current.get_next()
        else:
            previous.set_next(current.get_next())
