class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def find_pairs_with_sum(head, target_sum):
    pairs = []
    current = head
    
    while current:
        next_node = current.next
        while next_node:
            if current.data + next_node.data == target_sum:
                pairs.append((current.data, next_node.data))
            next_node = next_node.next
        current = current.next
    
    return pairs

# Helper function to print pairs
def print_pairs(pairs):
    for pair in pairs:
        print(pair)

# Example usage
keys = [1, 2, 3, 4, 5, 6]
target_sum = 7

# Create a doubly linked list
head = Node(keys[0])
current = head
for key in keys[1:]:
    new_node = Node(key)
    current.next = new_node
    new_node.prev = current
    current = new_node

print("Pairs with sum", target_sum, ":")
pairs = find_pairs_with_sum(head, target_sum)
print_pairs(pairs)
