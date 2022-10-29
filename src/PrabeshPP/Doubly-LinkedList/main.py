from IntNode import Node
from DoublyLinkedList import DoublyLinkedList

if __name__=="__main__":
    doublyLinkedList=DoublyLinkedList()
    doublyLinkedList.head=Node(2)
    secondNode=Node(10)
    thirdNode=Node(50)
    fourthNode=Node(60)
    doublyLinkedList.head.next=secondNode
    doublyLinkedList.head.prev=None
    secondNode.prev=doublyLinkedList.head
    secondNode.next=thirdNode
    thirdNode.prev=secondNode
    thirdNode.next=fourthNode
    fourthNode.prev=thirdNode
    fourthNode.next=None

    print("------------------All Node-----------------------------------")
    doublyLinkedList.printNode()

    doublyLinkedList.pushAtTheFront(7)
    doublyLinkedList.pushAtTheFront(9)
    doublyLinkedList.pushAtTheFront(19)
    print("[19]<--->[9]<--->[7]<--->[2]<--->[10]<--->[50]<--->[60]")
    doublyLinkedList.printNode()

    print("----------------------Add By Index----------------------------------")
    doublyLinkedList.addAtTheIndex(3,1)
    doublyLinkedList.addAtTheIndex(404,7)
    doublyLinkedList.printNode()

