from dataclasses import dataclass


class Node:
    def __init__(self,data,prev=None,next=None) -> None:
        self.data=data
        self.prev=None
        self.next=None