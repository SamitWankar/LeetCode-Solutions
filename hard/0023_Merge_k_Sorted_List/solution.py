import heapq


class Solution:
    def mergeKLists(self, lists):
        heap = []
        counter = 0

        # Put the first node of every non-empty list into the heap
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, counter, node))
                counter += 1

        # Dummy node helps us build the result
        dummy = ListNode(0)
        current = dummy

        # Process nodes until the heap is empty
        while heap:
            value, _, node = heapq.heappop(heap)

            # Add the smallest node to the result
            current.next = node
            current = current.next

            # Add the next node from the same list
            if node.next:
                heapq.heappush(
                    heap,
                    (node.next.val, counter, node.next)
                )
                counter += 1

        return dummy.next