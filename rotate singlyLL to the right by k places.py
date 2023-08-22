class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def rotateRight(head, k):
    if not head or k == 0:
        return head

    # Calculate the length of the linked list
    length = 1
    current = head
    while current.next:
        length += 1
        current = current.next
    
    # Calculate the effective rotation
    k %= length
    if k == 0:
        return head
    
    # Find the new head and tail of the rotated list
    new_head = head
    new_tail = head
    for i in range(length - k - 1):
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None
    
    # Connect the tail to the original head
    current = new_head
    while current.next:
        current = current.next
    current.next = head
    
    return new_head

# Helper function to convert a list to a linked list
def listToLinkedList(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to convert a linked list to a list
def linkedListToList(head):
    lst = []
    while head:
        lst.append(head.value)
        head = head.next
    return lst

# Example usage
input_list = [1, 2, 3, 4, 5]
k = 2
input_ll = listToLinkedList(input_list)
result_ll = rotateRight(input_ll, k)
result_list = linkedListToList(result_ll)
print(result_list)  # Output: [4, 5, 1, 2, 3]
