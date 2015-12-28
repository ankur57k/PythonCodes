from LinkedList import LinkedList
from Node import Node

head=Node(50)
ll=LinkedList(head)
print(ll.size())

ll.insert(2)
ll.printll()

ll.insert(5)
ll.printll()

ll.insert(10)
ll.printll()

ll.insert(2)
ll.printll()

print ll.search(5).get_data()
ll.printll()

print ll.search(2).get_data()
ll.printll()

ll.delete(2)
ll.printll()

ll.delete(10)
ll.printll()
