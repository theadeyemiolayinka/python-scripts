from IntNode import Node

class LinkedList:
    def __init__(self) -> None:
        self.head=None
        
    #adding to the front of the Linked List
    def addToFront(self,data):
        nodeToAdd=Node(data)
        nodeToAdd.next=self.head
        self.head=nodeToAdd
        
    # adding to the back of the Linked List
    
    def addToBack(self,data):
        temp=self.head
        
        nodeToAddBack=Node(data)
        
        #finding the last element in LinkedList
        while(temp.next!=None):
            temp=temp.next
        
        temp.next=nodeToAddBack
        nodeToAddBack.next=None
        
    
    # adding Node at the given index 

    def addToIndex(self,data,index):
        currNode=self.head
        prevNode=None
        elementToBeAdded=Node(data)
        i=0
        while(i<index and currNode!=None):
            prevNode=currNode
            currNode=currNode.next
            i=i+1
        
        if(currNode==None and i>index):
            print("invalid argument")
        
        else:
            prevNode.next=elementToBeAdded
            elementToBeAdded.next=currNode

        
    def removeFromFront(self):
        currNode=self.head
        self.head=currNode.next
        currNode=None
    
    def removeFromBack(self):
        currNode=self.head
        prevNode=None
        while(currNode.next!=None):
            prevNode=currNode
            currNode=currNode.next
        currNode=None
        prevNode.next=None
    
    def removeFromIndex(self,index):
        currNode=self.head
        currNode=self.head
        prevNode=None
        i=0
        while(i<index and currNode!=None):
            prevNode=currNode
            currNode=currNode.next
            i=i+1
        
        if(currNode==None and i>index):
            print("invalid argument")
        
        else:
            prevNode.next=currNode.next
            currNode=None

             
        
            
        
        
        
    #Traversing the LinkedList
    def printList(self):
        temp=self.head
        while(temp!=None):
            print(temp.data)
            temp=temp.next
            