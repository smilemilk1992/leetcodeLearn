'''
给定一个数M,求出大于该数的最小2的n次幂，返回n
'''
class Solution:
    def power(self, m: int) -> int:
        res=0
        while m>1:
            res=res+1
            m=m>>1
        return res

if __name__ == '__main__':
    s=Solution()
    m=17
    s.power(m)