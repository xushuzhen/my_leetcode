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
            i = 1
            while i < len(s):
                if s[i] in now_s:
                    i = start + 1
                    start = i
                end = i + 1
                now_s = s[start:end]
                temp_l = end - start
                if temp_l > l:
                    l = temp_l
                i += 1
            return l

    def lengthOfLongestSubstring3(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        start = 0
        d = {}
        for i, v in enumerate(s):
            if v in d and d[v] >= start:
                start = d[v] + 1
            d[v] = i
            result = max(result, i - start + 1)
        return result

    def lengthOfLongestSubstring4(self, s):
        """
        :type s: str
        :rtype: int
        """
        indexes = {}
        longest = 0
        last_repeating = -1
        for i, c in enumerate(s):
            if c in indexes and indexes[c] > last_repeating:
                last_repeating = indexes[c]
            if i - last_repeating > longest:
                longest = i - last_repeating
            indexes[c] = i
        return longest


if __name__ == '__main__':
    l = []
    l.append('abcabcbb')
    l.append('bbbbb')
    l.append('p')
    l.append('')
    l.append('dvdf')
    l.append('abcabd')
    l.append('abccabd')
    l.append('abcccabd')
    l.append('pwwkew')
    l.append('abcabdbbdefghhdefg')
    l.append('anviaj')
    solution = Solution()
    # print solution.lengthOfLongestSubstring(s)
    # print solution.lengthOfLongestSubstring2(s)
    for i, s in enumerate(l):
        print '%s\t%s\t%s' % (i, s, solution.lengthOfLongestSubstring2(s))
        print '%s\t%s\t%s' % (i, s, solution.lengthOfLongestSubstring4(s))
