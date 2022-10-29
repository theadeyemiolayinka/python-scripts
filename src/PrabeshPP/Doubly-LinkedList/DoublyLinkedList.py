from IntNode import Node

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head=None

    def pushAtTheFront(self,data):
        nodeToAdd=Node(data)
        nodeToAdd.next=self.head
        nodeToAdd.prev=None
        self.head=nodeToAdd

    def addAtTheIndex(self,data,index):
        if(index==0):
            self.pushAtTheFront(data)
        else:

            i=0
            elementToBeAdded=Node(data)
            prevNode=self.head
            currNode=self.head.next
            while(i<index-1 and currNode!=None):
                prevNode=currNode
                currNode=currNode.next
                i=i+1
            prevNode.next=elementToBeAdded
            elementToBeAdded.prev=prevNode
            elementToBeAdded.next=currNode
            currNode.prev=elementToBeAdded
        
    

    def printNode(self):
        currNode=self.head
        while(currNode!=None):
            print(currNode.data)
            currNode=currNode.next
    


    