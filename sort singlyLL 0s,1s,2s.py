class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def sort_linked_list(head):
    if not head or not head.next:
        return head

    # Count the occurrences of 0s, 1s, and 2s
    count_0 = 0
    count_1 = 0
    count_2 = 0
    current = head

    while current:
        if current.value == 0:
            count_0 += 1
        elif current.value == 1:
            count_1 += 1
        else:
            count_2 += 1
        current = current.next

    current = head
    # Update the linked list with the sorted values
    while current:
        if count_0 > 0:
            current.value = 0
            count_0 -= 1
        elif count_1 > 0:
            current.value = 1
            count_1 -= 1
        else:
            current.value = 2
            count_2 -= 1
        current = current.next

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
input_list = [1, 2, 0, 1, 2, 0, 1]
input_head = create_linked_list(input_list)
sorted_head = sort_linked_list(input_head)
sorted_list = linked_list_to_list(sorted_head)
print(sorted_list)  # Output: [0, 0, 1, 1, 1, 2, 2]
