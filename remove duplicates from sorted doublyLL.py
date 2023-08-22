class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def remove_duplicates(head):
    current = head
    
    while current and current.next:
        if current.data == current.next.data:
            next_next = current.next.next
            current.next = next_next
            if next_next:
                next_next.prev = current
        else:
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
keys = [1, 1, 2, 3, 3, 3, 4, 5, 5, 6, 6]
unique_head = Node(keys[0])
current = unique_head
for key in keys[1:]:
    new_node = Node(key)
    current.next = new_node
    new_node.prev = current
    current = new_node

print("Original linked list:")
print_list(unique_head)

# Remove duplicates
unique_head = remove_duplicates(unique_head)

print("Linked list after removing duplicates:")
print_list(unique_head)
