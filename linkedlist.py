

class Node:
    data: int = None
    next: "Node" = None

    def __init__(self, data: int):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"<Node data={self.data} />"


class LinkedList:
    head: Node = None

    def __init__(self, head: Node = None):
        self.head = head

    def insert_at_head(self, node: Node):
        """Insert a node at the beginning of the linked list"""
        node.next = self.head
        self.head = node

    def insert_at_tail(self, node: Node):
        """Insert a node at the end of the linked list"""
        if self.is_empty():
            self.head = node
            return True

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node

    def insert_before(self, node: Node, data: int) -> bool:
        """Given a node and a data value, insert the node
        in the list before the node with given data value
        """
        current = self.head
        prev = None
        while current is not None and current.data != data:
            prev = current
            current = current.next

        if current is not None and current.data == data:
            prev.next = node
            node.next = current
            return True
        
        return False

    def insert_after(self, node: Node, data: int) -> bool:
        """Given a node and a data value, insert the node
        in the list after the node with given data value.
        """
        current = self.head
        while current is not None and current.data != data:
            current = current.next

        if current is not None and current.data == data:
            next = current.next
            current.next = node
            node.next = next
            return True
        
        return False
        
    def delete_node(self, data: int):
        """Given a data value, remove that node from the LinkedList"""
        if self.is_empty():
            return False
        
        current = self.head
        prev = None
        while current is not None and current.data != data:
            prev = current
            current = current.next

        if current is not None and current.data == data:
            prev.next = current.next
            return True
        return False
        
    def traverse(self):
        """Return values in LinkedList in order, as a Python list."""
        if self.is_empty():
            return []
        
        values: list[int] = []
        current = self.head
        while current is not None:
            values.append(current.data)
            current = current.next

        return values
    
    def search(self, data: int):
        """Given a data value, find the Node in the list with that value
        and return the Node; if Node not found, returns None
        """
        if self.is_empty():
            return None
        
        current = self.head
        while current is not None:
            if current.data == data:
                return current
            current = current.next
        return None

    def reverse(self):
        """Reverse the contents of the list and returns the new head node."""
        if self.is_empty():
            return None
        
        current = self.head
        prev = None
        while current is not None:

            next_node = current.next
            current.next = prev
            prev = current

            if next_node is None:
                self.head = current

            current = next_node

        return self.head

    def rotate(self, k: int = 0):
        """Rotates the list k times and returns the final head node.
        One rotation moves the tail element to the head.
        """
        if self.head is None or k == 0:
            return self.head

        for _ in range(k):
            # set current to tail
            tail = self.head
            penultimate = None
            while tail.next is not None:
                penultimate = tail
                tail = tail.next

            tail.next = self.head
            self.head = tail
            if penultimate is not None:
                penultimate.next = None

        return self.head
    
    def is_palindrome(self):
        values = self.traverse()
        if not values:
            return True
        return values == values[::-1]
    
    def is_empty(self):
        return self.head is None
    
    def merge(self, other_list: "LinkedList"):
        """Given two sorted LinkedLists, merge them into a new sorted LinkedList and return"""
        if self.is_empty():
            self.head = other_list.head
            return self.head
        
        merged = LinkedList()

        current = self.head
        other = other_list.head

        while current is not None or other is not None:
            if current is not None and other is not None:
                if current.data < other.data:
                    merged.insert_at_tail(Node(data=current.data))
                    current = current.next
                else:
                    merged.insert_at_tail(Node(data=other.data))
                    other = other.next
            elif current is not None:
                merged.insert_at_tail(Node(data=current.data))
                current = current.next
            elif other is not None:
                merged.insert_at_tail(Node(data=other.data))
                other = other.next

        return merged
    
    def sort(self):
        """TODO: Sort the list in place using MergeSort"""
        pass



class DoublyLinkedNode(Node):
    prev: "Node" = None

    def __init__(self, data: int):
        super().__init__(data)
        self.prev = None
