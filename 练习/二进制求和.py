class Solution(object):
    def addBinary(self, a, b):
        res = ''
        lsa, lsb = len(a), len(b)
        pos, plus, curr = -1, 0, 0
        while (lsa + pos) >= 0 or (lsb + pos) >= 0:
            print("lsa={},pos={}".format(lsa,pos))
            if (lsa + pos) >= 0:
                curr += int(a[pos])
                print("1curr={}".format(curr))
            if (lsb + pos) >= 0:
                curr += int(b[pos])
                print("2curr={}".format(curr))
            res = str(curr % 2) + res
            curr //= 2
            pos -= 1
        if curr == 1:
            res = '1' + res
        return res
# %%
s = Solution()
print(s.addBinary(a = "1010", b = "1011"))