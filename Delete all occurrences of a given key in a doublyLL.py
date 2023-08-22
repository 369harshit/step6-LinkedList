class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def delete_key(head, key):
    # Handle the case where the list is empty
    if head is None:
        return None

    # Traverse the list and delete nodes with the given key
    current = head
    while current:
        if current.data == key:
            # Update pointers of previous and next nodes
            if current.prev:
                current.prev.next = current.next
            if current.next:
                current.next.prev = current.prev
            if current == head:
                head = current.next
        current = current.next

    return head

# Helper function to print the doubly linked list
def print_list(head):
    current = head
    while current:
        print(current.data, end=" <-> ")
        current = current.next
    print("None")

# Example usage
keys = [2, 3, 2, 5, 2, 7]
key_to_delete = 2

# Create a doubly linked list
head = Node(keys[0])
current = head
for key in keys[1:]:
    new_node = Node(key)
    current.next = new_node
    new_node.prev = current
    current = new_node

print("Original linked list:")
print_list(head)

# Delete all occurrences of the key
head = delete_key(head, key_to_delete)

print("Linked list after deleting key:", key_to_delete)
print_list(head)
