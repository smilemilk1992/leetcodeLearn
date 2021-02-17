__author__ = 'haochen214934'


class Solution:
    def traverse(self, Lists):
        m=len(Lists)
        n=len(Lists[0])
        flag=[[False]*n for _ in range(m)]
        i=0
        j=0
        temp=1 #1 下 2 右 3 上 4 左
        result=[]
        while True:
            if i>=n or j>=n or flag[i][j]:
                break
            result.append(Lists[i][j])
            flag[i][j]=True
            if temp==1:
                if i==m-1 or flag[i+1][j]:
                    j = j + 1
                    temp=2
                else:
                    i = i + 1
            elif temp==2:
                if j==n-1 or flag[i][j+1]:
                    i = i - 1
                    temp=3
                else:
                    j = j + 1
            elif temp==3:
                if i==0 or flag[i-1][j]:
                    j = j - 1
                    temp=4
                else:
                    i = i - 1
            elif temp==4:
                if flag[i][j-1]:
                    i = i + 1
                    temp=1
                else:
                    j = j - 1

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
