# Package to create a singly-linked list from a Python list, and vice versa

from typing import List, Any, Union

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def list_to_linked(lst: List[Any]) -> Union[ListNode, None]:
    head = last = None

    for elem in lst:
        curr = ListNode(elem)
        if head is None:
            head = curr
            prev = curr
        else:
            prev.next = curr
            prev = curr

    return head

def linked_to_list(head: ListNode) -> Union[ListNode, None]:
    lst = []

    curr = head
    while curr is not None:
        lst.append(curr.val)
        curr = curr.next

    return lst

# A direct and simple test of the two conversion functions
if __name__ == '__main__':
    lst_1 = [1,4,3,2,5,2]
    lnked_1 = list_to_linked(lst_1)
    back_to_list = linked_to_list(lnked_1)

    print(lst_1)
    print(back_to_list)
