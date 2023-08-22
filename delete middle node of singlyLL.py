class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def delete_middle_node(head):
    if not head or not head.next:
        return None

    slow = head
    fast = head
    prev = None

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    if prev:
        prev.next = slow.next
    else:
        head = head.next

    return head

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
reordered_head = delete_middle_node(input_head)
reordered_list = linked_list_to_list(reordered_head)
print(reordered_list)  # Output: [1, 2, 4, 5]
