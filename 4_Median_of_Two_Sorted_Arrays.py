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

    def findMedianSortedArrays2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1 = nums1 + nums2
        nums1.sort()
        l = len(nums1)
        if l == 0:
            return 0.0
        m = l % 2
        a = l / 2
        if m > 0:
            return float(nums1[a])
        else:
            return float(nums1[a] + nums1[a - 1]) / 2

    def findMedianSortedArrays3(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        all_nums = nums1 + nums2
        print nums1, nums2, all_nums
        len_all = len(all_nums)
        all_nums.sort()

        if len_all == 0:
            return None
        elif len_all == 1:
            return all_nums[0]
        elif len_all == 2:
            return ((all_nums[0] + all_nums[1]) / 2.0)

        if len_all % 2 == 0:
            median = (all_nums[(len(all_nums) / 2)] + all_nums[(len(all_nums) / 2) - 1]) / 2.0
        else:
            median = all_nums[(len(all_nums) / 2)]

        return median


if __name__ == '__main__':
    solution = Solution()
    n1 = [1, 2]
    n2 = [3, 4]
    n3 = [1, 3]
    n4 = []
    n5 = [1]
    n6 = [2, 3]
    # print solution.findMedianSortedArrays2(n1, n2)
    # print solution.findMedianSortedArrays2(n3, n4)
    # print solution.findMedianSortedArrays2(n5, n6)
    # print solution.findMedianSortedArrays2(n4, n4)
    # print solution.findMedianSortedArrays2(n4, n5)
    print solution.findMedianSortedArrays3(n4, n5)
