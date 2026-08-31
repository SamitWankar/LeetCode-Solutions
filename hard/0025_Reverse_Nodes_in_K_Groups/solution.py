class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head

        group_prev = dummy

        while True:
            # Find the kth node
            kth = group_prev

            for _ in range(k):
                kth = kth.next
                if kth is None:
                    return dummy.next

            # Node after the current group
            group_next = kth.next

            # Save the first node of the group
            group_start = group_prev.next

            # Reverse k nodes
            prev = group_next
            curr = group_start

            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Connect previous part to reversed group
            group_prev.next = prev

            # Move to the next group
            group_prev = group_start