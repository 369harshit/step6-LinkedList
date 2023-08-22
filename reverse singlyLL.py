class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    if not head or not head.next:
        return head
    
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return prev

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to convert a linked list to a list of values
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result

# Example usage
input_list = [1, 2, 3, 4, 5]
input_head = create_linked_list(input_list)
reversed_head = reverse_linked_list(input_head)
reversed_list = linked_list_to_list(reversed_head)
print(reversed_list)  # Output: [5, 4, 3, 2, 1]
