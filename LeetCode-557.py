#-*-coding=utf-8-*-
#1
class Solution(object):
    def reverseSent(self,s):
        return ' '.join(w[::-1] for w in s.split())


s=Solution()
rs=s.reverseSent('hehe zhen jia')
print(rs)

import math
#2
class Solution2(object):
    def reverseS2(self,s):
        slist=list(s)
        slen=len(s)
        p=q=0
        while p<slen:
            while q<slen and s[q]!=' ':  
                q+=1
            for x in range (math.ceil((q-p)/2)):
                slist[p+x],slist[q-1-x]=slist[q-1-x],slist[p+x]
            p=q=q+1
        return ''.join(slist) 
        #return slist

s2=Solution2()
r2=s2.reverseS2('hi sw sf')
print(r2)
