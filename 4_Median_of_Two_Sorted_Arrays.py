class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        ln1 = len(nums1)
        ln2 = len(nums2)
        if ln1 == 0:
            return self.getIndex(nums2)
        elif ln2 == 0:
            return self.getIndex(nums1)
        else:
            return (self.getIndex(nums1) + self.getIndex(nums2)) / 2

    def getIndex(self, nums):
        import math
        ln = float(len(nums))
        if ln > 0:
            avgl = int(math.ceil(ln / 2))
            m = ln % 2
            median = 0.0
            if m > 0:
                median = float(nums[avgl - 1])
            else:
                median = float(nums[avgl - 1] + nums[avgl]) / 2
            return median
        else:
            return 0.0


if __name__ == '__main__':
    solution = Solution()
    n1 = [1, 2]
    n2 = [3, 4]
    n3 = [1, 3]
    n4 = []
    n5 = [1]
    n6 = [2, 3]
    print solution.findMedianSortedArrays(n1, n2)
    print solution.findMedianSortedArrays(n3, n4)
    print solution.findMedianSortedArrays(n5, n6)
