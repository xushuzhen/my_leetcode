class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {
            'I': 1,
            'i': 1,
            'V': 5,
            'v': 5,
            'X': 10,
            'x': 10,
            'L': 50,
            'l': 50,
            'C': 100,
            'c': 100,
            'D': 500,
            'd': 500,
            'M': 1000,
            'm': 1000
        }
        b = 0
        c = 0
        for i in range(len(s)-1, -1, -1):
            a = d[s[i]]
            if a < b:
                c = c - a
            else:
                c = c + a
            b = d[s[i]]
        return c


if __name__ == '__main__':
    solution = Solution()
    s = 'III'
    s1 = 'IV'
    s2 = 'VI'
    s3 = 'VII'
    s4 = 'VIII'
    s5 = 'MCMXCVI'
    print solution.romanToInt(s)
    print solution.romanToInt(s1)
    print solution.romanToInt(s2)
    print solution.romanToInt(s3)
    print solution.romanToInt(s4)
    print solution.romanToInt(s5)
