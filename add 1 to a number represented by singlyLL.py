class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def addOneToLinkedList(head):
    dummy = ListNode(0)
    dummy.next = head
    
    # Find the rightmost non-nine node
    non_nine = dummy
    while head:
        if head.value != 9:
            non_nine = head
        head = head.next
    
    # Increment the rightmost non-nine node
    non_nine.value += 1
    
    # Update all following nodes to be zero
    current = non_nine.next
    while current:
        current.value = 0
        current = current.next
    
    if dummy.value == 1:
        return dummy
    else:
        dummy.next

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
input_list = [9, 9, 9]
input_ll = listToLinkedList(input_list)
result_ll = addOneToLinkedList(input_ll)
result_list = linkedListToList(result_ll)
print(result_list)  # Output: [1, 0, 0, 0]
