class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_at_beginning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at the end
    def insert_at_end(self,data):
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
            print(temp.data, end="-->")
            temp = temp.next
        print("None")
    
    # Delete a node
    def delete_node(self, key):
        temp = self.head

        # if head node itself holds the key
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
l1 = LinkedList()
l1.insert_at_beginning(1)
l1.insert_at_beginning(4)
l1.insert_at_end(2)
l1.insert_at_end(7)
l1.traverse()
l1.delete_node(4)
l1.traverse()



        

        