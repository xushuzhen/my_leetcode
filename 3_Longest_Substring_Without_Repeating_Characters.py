class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        else:
            start = 0
            end = 1
            l = 1
            now_s = s[start:end]
            result = now_s
            for i in range(1, len(s)):
                if s[i] not in now_s:
                    end = i + 1
                    now_s = s[start:end]
                    temp_l = end - start
                    if temp_l > l:
                        result = now_s
                        l = temp_l
                else:
                    i = i - 1
                    start = i
                    end = i + 1
                    now_s = s[start:end]
            return result
            # return l

    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        else:
            start = 0
            end = 1
            now_s = s[start:end]
            l = 1
            result = now_s
            i = 1
            while i < len(s):
                if s[i] in now_s:
                    i = start + 1
                    start = i
                end = i + 1
                now_s = s[start:end]
                temp_l = end - start
                if temp_l > l:
                    result = now_s
                    l = temp_l
                i += 1
            # return result
            return l

    def lengthOfLongestSubstring3(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        left = 0
        d = {}

        for i, ch in enumerate(s):
            if ch in d and d[ch] >= left:
                left = d[ch] + 1
            d[ch] = i
            res = max(res, i - left + 1)
        return res


if __name__ == '__main__':
    l = []
    # l.append('abcabcbb')
    # l.append('bbbbb')
    # l.append('p')
    # l.append('')
    # l.append('dvdf')
    # l.append('abcabd')
    # l.append('abccabd')
    # l.append('abcccabd')
    # l.append('pwwkew')
    l.append('abcabdbbdefghhdefg')
    # l.append('anviaj')
    solution = Solution()
    # print solution.lengthOfLongestSubstring(s)
    # print solution.lengthOfLongestSubstring2(s)
    for i, s in enumerate(l):
        print '%s\t%s\t%s' % (i, s, solution.lengthOfLongestSubstring3(s))
