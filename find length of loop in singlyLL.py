class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def find_loop_length(head):
    slow = head
    fast = head
    loop_found = False
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            loop_found = True
            break

    if not loop_found:
        return 0

    count = 1
    current = slow.next
    while current != slow:
        count += 1
        current = current.next

    return count

# Example usage
# Create a linked list with a loop
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node3  # Creating a loop

loop_length = find_loop_length(node1)
print("Loop length:", loop_length)  # Output: Loop length: 3
