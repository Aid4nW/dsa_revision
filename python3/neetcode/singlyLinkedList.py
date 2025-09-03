from typing import List

class LinkedList:
    
    def __init__(self):
        self.current_head: Node|None = None
    
    def get(self, index: int) -> int:

        current_node = self.current_head
        counter = 0

        while current_node != None:
            if counter == index:
                return current_node.value

            current_node = current_node.next
            counter += 1
        
        return -1

    def insertHead(self, val: int) -> None:
        old_head = self.current_head
        self.current_head = Node(val, old_head)

    def insertTail(self, val: int) -> None:
        if self.current_head != None:
            # List has nodes
            last_node = self.current_head
            current_node = self.current_head.next

            while current_node != None:
                last_node = current_node
                current_node = current_node.next
            
            last_node.setNext(Node(val))

        else:
            # List is empty
            self.current_head = Node(val)
        

    def remove(self, index: int) -> bool:
        if self.current_head != None:
            if index == 0:
                # If index is zero we're removing the first Node
                self.current_head = self.current_head.next
                return True

            # List has nodes, and we're removing something besides Node 0
            previous_node = self.current_head
            current_node = self.current_head.next
            counter = 1

            while current_node != None:
                if counter == index:
                    # Correct node found
                    previous_node.setNext(current_node.next)
                    return True

                previous_node = current_node
                current_node = current_node.next
                counter += 1
            
        # Index is out of bounds
        return False
        

    def getValues(self) -> List[int]:
        output = []
        current_node = self.current_head

        while current_node != None:
            output.append(current_node.value)
            current_node = current_node.next
        
        return output
        
class Node:

    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def setNext(self, next):
        self.next = next