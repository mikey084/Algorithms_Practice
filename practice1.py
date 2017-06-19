'''
https://www.interviewcake.com/question/python/reverse-linked-list

Write a function that can reverse a linked list and does it in-place.

Strategy:

'''


class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return "value:{}".format(self.value)


# reverses it, and returns new head
def reverse_linked_list(head):
    current = head
    prev = None
    old_next = None

    while current:
        # node we will visit next
        old_next = current.next
        # point the current node to previous
        current.next = prev
        # shuffle the prev to the current node as we move along the list
        prev = current
        # shuffle current to the next node in the list
        current = old_next

    # new head since current is None and we reached end of original list
    return prev

def print_linked_list(head):
    node = head
    output = []
    while node:
        output.append(node.value)
        node = node.next

    print(output)

a = LinkedListNode(1)
b = LinkedListNode(2)
c = LinkedListNode(3)
a.next = b
b.next = c

print_linked_list(a)
print(print_linked_list(reverse_linked_list(a)))


for x in range(10):
    print(str(x) + '\n')