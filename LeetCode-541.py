import math

class Solution(object):
    def ReverseStr(self, str, k):
        ans=''
        n = int (math.ceil(len(str) / (2.0*k) ))
        for i in range(n):
            ans += str[2*i*k:(2*i+1)*k][::-1] #reverse k str
            print '1',ans
            ans += str[(2*i+1)*k:(2*i+2)*k]
            print '2',ans
        return ans



rs=Solution()
print rs.ReverseStr('sjodfjoig',3)

s='sjodfjoig'
print s[0:1]

a=''
a += s[8:20]
print s[10]    #why???
print s[10:12] #
print 'a=',a
