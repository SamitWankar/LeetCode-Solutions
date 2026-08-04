from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Always perform binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        # Number of elements that should be on the left side
        left_size = (m + n + 1) // 2

        low = 0
        high = m

        while low <= high:

            # Partition in nums1
            partitionX = (low + high) // 2

            # Partition in nums2
            partitionY = left_size - partitionX

            # Elements around partitionX
            leftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            rightX = float('inf') if partitionX == m else nums1[partitionX]

            # Elements around partitionY
            leftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            rightY = float('inf') if partitionY == n else nums2[partitionY]

            # Correct partition found
            if leftX <= rightY and leftY <= rightX:

                # Odd total elements
                if (m + n) % 2 == 1:
                    return max(leftX, leftY)

                # Even total elements
                return (max(leftX, leftY) + min(rightX, rightY)) / 2

            # Move partition to the left
            elif leftX > rightY:
                high = partitionX - 1

            # Move partition to the right
            else:
                low = partitionX + 1