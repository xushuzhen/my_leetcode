import datetime


class Solution(object):
    def reverse(self, x):
        max_int32 = 2147483647
        min_int32 = -2147483648
        if max_int32 >= x >= min_int32:
            r_str = ''
            x_str = str(x)
            if x_str[0] == '-':
                r_str += '-'
                x_str = x_str[1:]
            for i in xrange(len(x_str) - 1, -1, -1):
                r_str += x_str[i]
            r = int(r_str)
            return r if max_int32 >= r >= min_int32 else 0
        else:
            return 0

    def reverse1(self, x):
        str_x = str(x)
        rev = list(str_x)
        rev.reverse()
        rev = "".join(rev)
        if rev[-1] == '-':
            rev = -int(rev[:-1])
        else:
            rev = int(rev)
        if rev > 2147483647 or rev < -2147483648:
            return 0
        else:
            return rev

    def reverse2(self, x):
        a = 1
        if x < 0:
            a = -1
            x = -x
        res = 0
        while x > 0:
            res = res * 10 + x % 10
            x = x / 10
        if abs(res) > 0x7FFFFFFF:
            return 0
        return res * a


if __name__ == '__main__':
    a = 123
    b = -123
    c = 2147483648
    d = 2147483647
    e = -2147483649
    f = -2147483648
    g = 1324554321
    h = -1324554321
    getIndices = Solution()
    # print getIndices.reverse(a)
    # print getIndices.reverse(b)
    # print getIndices.reverse(c)
    # print getIndices.reverse(d)
    # print getIndices.reverse(e)
    # print getIndices.reverse(f)
    # print getIndices.reverse(g)
    begin = datetime.datetime.now()
    aa = getIndices.reverse(h)
    end = datetime.datetime.now()
    print aa, end - begin

    begin = datetime.datetime.now()
    aa = getIndices.reverse1(h)
    end = datetime.datetime.now()
    print aa, end - begin

    begin = datetime.datetime.now()
    aa = getIndices.reverse2(h)
    end = datetime.datetime.now()
    print aa, end - begin
    aaaa = '1234'
    bbbb = [1, 2, 3, 4, 1]
    bbbb.reverse()
    print bbbb
    print bbbb.sort()
    aaaa.reverse()
    print aaaa
    a = [5, 7, 6, 3, 4, 1, 2]
    a.sort()
    print a
