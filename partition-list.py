from list_to_linked import ListNode, list_to_linked, linked_to_list


class Solution:
    def partition_1(self, head: ListNode, x: int) -> ListNode:
        # Maintain two refs p1 and p2 that form the boundary of the partitioning
        # between nodes smaller than x and nodes equal to or greater than x.
        # p1 points to the rightmost smaller node, p2 points to the leftmode equal/bigger node.
        # p1 will shift to the right as smaller nodes are added, while p2 does not change once found.

        # Iterate once through the list, processing each node.

        p1 = p2 = None
        prev = None
        curr = head
        while curr is not None:
            if curr.val < x:
                if p2 is None:  # No large nodes found yet
                    prev = curr
                    curr = curr.next
                    p1 = prev
                elif p1 is None:  # Large nodes already found, this is the first small node
                    temp = curr

                    prev.next = curr.next  # Remove this node from its original position
                    curr = curr.next

                    temp.next = head  # Insert this node at the head of the list
                    head = temp

                    p1 = temp
                else:  # Both p1 and p2 are not None
                    temp = curr

                    prev.next = curr.next  # Remove this node
                    curr = curr.next

                    temp.next = p2  # Insert this node at the boundary
                    p1.next = temp

                    p1 = temp
            else:  # curr.val >= x
                if p2 is None:  # This is the first large node seen
                    p2 = curr
                prev = curr
                curr = curr.next

        return head

    def partition_2(self, head: ListNode, x: int) -> ListNode:
        # Build two sublists, one for small nodes, the other for large nodes.
        # Iterate once through the list, processing each node.
        # If it's a small node, append it to the small list. Likewise, if it's
        # a large node, append it to the large list.

        # After every node has been added to one of the two lists, append the list
        # of large nodes to the small one, and return the head to the small list.

        head_small = last_small = None
        head_large = last_large = None

        # Iterate through the linked list, adding each node to either the small linked list
        # or the large linked list.
        curr = head
        while curr is not None:
            nxt = curr.next

            if curr.val < x:
                if head_small is None:
                    head_small = curr
                    last_small = curr
                else:
                    last_small.next = curr
                    last_small = curr
            else:  # curr.val <= x
                if head_large is None:
                    head_large = curr
                    last_large = curr
                else:
                    last_large.next = curr
                    last_large = curr
            curr.next = None

            curr = nxt

        # Append the linked list of large nodes to the linked list of small nodes.
        if last_small is not None:
            last_small.next = head_large
            return head_small
        else:  # There were no small numbers
            return head_large


if __name__ == '__main__':
    lst_1 = [1, 4, 3, 2, 5, 2]
    x = 3
    print(lst_1, x)

    lnked_1 = list_to_linked(lst_1)
    result1 = Solution().partition_1(lnked_1, x)
    back_to_list1 = linked_to_list(result1)
    print(back_to_list1)

    lnked_2 = list_to_linked(lst_1)
    result2 = Solution().partition_2(lnked_2, x)
    back_to_list2 = linked_to_list(result2)
    print(back_to_list2)
