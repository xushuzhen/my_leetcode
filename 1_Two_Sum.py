class Solution(object):
    def twoSum(self, nums, target):
        for i in xrange(0, len(nums) - 1):
            for j in xrange(i + 1, len(nums)):
                numSum = nums[i] + nums[j]
                if numSum == target:
                    return [i, j]

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    getIndices = Solution()
    print getIndices.twoSum(nums, target)