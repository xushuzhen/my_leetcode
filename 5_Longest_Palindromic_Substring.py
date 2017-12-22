class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        l = len(s)
        for i in range(0, l):
            for j in range(i, l):
                t = s[i: j + 1]
                p = self.is_palindrome(t)
                if p and len(t) > len(result):
                    result = t
        return result

    def is_palindrome(self, s):
        l = len(s)
        m = l / 2
        for i in range(0, m):
            if s[i] != s[l - 1 - i]:
                return False
        return True

    def longestPalindrome2(self, s):
        l = len(s)
        if l < 1:
            return None
        elif l < 3:
            return s
        else:
            pass


if __name__ == '__main__':
    solution = Solution()
    s = 'abccba'
    s1 = 'abcba'
    s2 = 'abcde'
    s3 = 'abbcccabcba'
    s4 = 'z'
    s5 = 'hj'
    print solution.longestPalindrome2(s)
    print solution.longestPalindrome2(s1)
    print solution.longestPalindrome2(s2)
    print solution.longestPalindrome2(s3)
    print solution.longestPalindrome2(s4)
    print solution.longestPalindrome2(s5)
