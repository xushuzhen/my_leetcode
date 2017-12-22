class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        l = len(s)
        m = l / 2
        for i in range(0, m):
            if s[i] != s[l - 1 - i]:
                return False
        return True

    def isPalindrome1(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        reverse = x[::-1]
        if x == reverse:
            return True
        return False


if __name__ == '__main__':
    solution = Solution()
    s = 12321
    print solution.isPalindrome(s)
