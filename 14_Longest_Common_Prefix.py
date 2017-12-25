class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        trans = zip(*strs)
        l = ''
        for i in trans:
            s = list(set(i))
            if len(s) == 1:
                l += s[0]
            else:
                return l
        return l


if __name__ == '__main__':
    solution = Solution()
    s = [''
         ]
    print solution.longestCommonPrefix(s)
