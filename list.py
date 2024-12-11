class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Traverse and print the linked list
    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # Delete a node
    def delete_node(self, key):
        temp = self.head

        # If head node itself holds the key
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        # Search for the key
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        # Key not found
        if not temp:
            return

        # Unlink the node
        prev.next = temp.next
        temp = None

# Example Usage
ll = LinkedList()
ll.insert_at_beginning(1)
# ll.insert_at_beginning(2)
# ll.insert_at_end(4)
# ll.insert_at_end(5)
ll.traverse()  # Output: 2 -> 3 -> 4 -> 5 -> None
# ll.delete_node(3)
# ll.traverse()  # Output: 2 -> 4 -> 5 -> None
