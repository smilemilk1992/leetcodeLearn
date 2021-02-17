__author__ = 'haochen214934'


class Solution:
    def traverse(self, Lists):
        m=len(Lists)
        n=len(Lists[0])
        flag=[[0]*n for _ in range(m)]
        flag[0][0]=Lists[0][0]
        for i in range(1,m):
            flag[i][0]=flag[i-1][0]+Lists[i][0]
        for j in range(1,n):
            flag[0][j]=flag[0][j-1]+Lists[0][j]
        for i in range(1,m):
            for j in range(1,n):
                flag[i][j]=min(flag[i-1][j]+Lists[i][j],flag[i][j-1]+Lists[i][j])
        return flag[-1][-1]


if __name__ == '__main__':
    s = Solution()
    #[[1, 4, 5], [2, 7, 6], [6, 8, 7]]
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    f=s.traverse(matrix)
    print(f)
