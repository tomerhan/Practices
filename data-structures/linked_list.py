"""
Linked List
-----------
A singly linked list implementation demonstrating node-based data structures.

Operations and time complexity:
- append      : O(n)
- prepend     : O(1)
- delete      : O(n)
- search      : O(n)
- to_list     : O(n)
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        """Insert a new node at the beginning of the list."""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def append(self, value):
        """Insert a new node at the end of the list."""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, value):
        """Remove the first node with the given value. Return True if removed."""
        if self.head is None:
            return False
        if self.head.value == value:
            self.head = self.head.next
            return True
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return True
            current = current.next
        return False

    def search(self, value):
        """Return the node containing value, or None if not found."""
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def to_list(self):
        """Convert the linked list to a Python list."""
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def __repr__(self):
        return " -> ".join(str(v) for v in self.to_list())


if __name__ == "__main__":
    ll = LinkedList()
    for value in [1, 2, 3, 4, 5]:
        ll.append(value)
    print(f"Initial list:       {ll}")

    ll.prepend(0)
    print(f"After prepend(0):   {ll}")

    ll.delete(3)
    print(f"After delete(3):    {ll}")

    node = ll.search(4)
    print(f"Search for 4:       {'found' if node else 'not found'}")
