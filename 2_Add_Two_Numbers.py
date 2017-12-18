# class ListNode(object):
#     def __init__(self, v, p=None):
#         self.val = v
#         self.next = p
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList(object):
    def __init__(self, in_str):
        self.str = in_str
        self.ls = len(self.str)
        if self.ls == 0:
            self.head = None
        else:
            self.head = ListNode(int(self.str[0]))
            p = self.head
            for i in self.str[1:]:
                p.next = ListNode(int(i))
                p = p.next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        lr = None
        if not l1:
            return l2
        elif not l2:
            return l1
        elif not l1 and not l2:
            return lr
        p1 = l1
        p2 = l2
        t = p1.val + p2.val
        s = t % 10
        a = t / 10
        head = ListNode(s)
        ph = head
        while True:
            if not p1.next and not p2.next:
                break
            if p1.next:
                p1 = p1.next
                v1 = p1.val
            else:
                v1 = 0
            if p2.next:
                p2 = p2.next
                v2 = p2.val
            else:
                v2 = 0
            t = v1 + v2 + a
            s = t % 10
            a = t / 10
            ph.next = ListNode(s)
            ph = ph.next
        if a != 0:
            ph.next = ListNode(a)
        return head


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head = ListNode(0)
        node = head
        carryOver = 0
        while True:
            value1 = l1.val if l1 is not None else 0
            value2 = l2.val if l2 is not None else 0
            node.val = (value1 + value2 + carryOver) % 10
            carryOver = (value1 + value2 + carryOver) / 10
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            if l1 or l2:
                node.next = ListNode(0)
                node = node.next
            else:
                break
        if carryOver:
            node.next = ListNode(1)
        return head


# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         lr = []
#         a1 = len(l1)
#         a2 = len(l2)
#         c1 = 0
#         c2 = 0
#         a = 0
#         while True:
#             if not c1 < a1 and not c2 < a2:
#                 break
#             if c1 < a1:
#                 v1 = l1[c1]
#                 c1 += 1
#             else:
#                 v1 = 0
#             if c2 < a2:
#                 v2 = l2[c2]
#                 c2 += 1
#             else:
#                 v2 = 0
#             s = (v1 + v2 + a) % 10
#             a = (v1 + v2) / 10
#             lr.append(s)
#         if a != 0:
#             lr.append(a)
#         return lr

if __name__ == '__main__':
    l1 = LinkedList('1').head
    l2 = LinkedList('999').head
    getlr = Solution()
    lr = getlr.addTwoNumbers(l1, l2)
    print lr.val, lr.next.val, lr.next.next.val, lr.next.next.next.val
    #
    # getlr = Solution()
    # lr = getlr.addTwoNumbers([1], [1])
    # print lr
    #
    # l = 0
    # if l == 1:
    #     val = l
    # else:
    #     val = 0
    #
    # print val
    # val = l if l == 1 else 0
    # print val
    # print sum(range(1, 101))
    # print reduce(lambda x, y: x + y, range(1, 101))
    # print [x for x in range(1, 101) if x % 2 == 0]
    # print reduce(lambda x, y: x + 2, range(1, 101))
    # print [x for x in range(1, 101) if x % 2 == 0]
    # print filter(lambda x: x % 2 == 0, range(1, 101))
