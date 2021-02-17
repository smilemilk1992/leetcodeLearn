__author__ = 'haochen214934'


class Solution:
    def traverse(self, Lists):
        m=len(Lists)
        n=len(Lists[0])
        i=0
        j=0
        temp=1 #1 右 2 左
        result=[]
        while True:
            if i>=m or j>=n:
                break
            result.append(Lists[i][j])
            if temp==1:
                if j==n-1:
                    i=i+1
                    temp=2
                else:
                    j=j+1
            elif temp==2:
                if j==0:
                    i=i+1
                    temp=1
                else:
                    j=j-1




        print(result)


if __name__ == '__main__':
    s = Solution()
    matrix = [
        [1,  4,  7,  11, 15],
        [2,  5,  8,  12, 19],
        [3,  6,  9,  16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    s.traverse(matrix)
