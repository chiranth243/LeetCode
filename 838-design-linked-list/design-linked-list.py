class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val
        

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.size += 1


    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size: return
        if index <= 0: return self.addAtHead(val)
        if index == self.size: return self.addAtTail(val)

        new_node = Node(val)
        prev = self.head
        for _ in range(index - 1):
            prev = prev.next
        
        new_node.next = prev.next
        prev.next = new_node
        self.size += 1


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size: return

        if index == 0:
            self.head = self.head.next
            if self.size == 1: 
                self.tail = None
        else:
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next
            
            prev.next = prev.next.next
            if index == self.size - 1:
                self.tail = prev
        
        self.size -= 1
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)