from IntNode import Node
from LinkedList import LinkedList




if __name__=="__main__":
    llist=LinkedList()
    llist.head=Node(3)
    secondNode=Node(10)
    thirdNode=Node(20)
    
    
    # Linking two nodes
    llist.head.next=secondNode
    secondNode.next=thirdNode
    
    #adding node at the front of the linked list
    # ---------------------------Add To Front------------------------------------------
    llist.addToFront(300)
    llist.addToFront(2)
    llist.addToFront(700)
    
    
    #adding node at the back of the linked list
    # ---------------------------Add To Back-------------------------------------------
    llist.addToBack(55)
    llist.addToBack(555)
    llist.addToBack(5555)
    
    llist.addToIndex(121,5)
    
    
    
    #printing all the Node of the Linked List``
    llist.printList()
    print("---------------------------Remove From Front------------------------------------")
    llist.removeFromFront()
    llist.printList()
    print("-----------------------------Remove from Back-------------------------------------")
    llist.removeFromBack()
    llist.printList()
    print("-----------------------------Remove from given Index-------------------------------------")
    llist.removeFromIndex(3)
    llist.printList()
    