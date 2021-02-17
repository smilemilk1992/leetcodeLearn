__author__ = 'haochen214934'


class Solution:
    def traverse(self, Lists):
        res=[Lists[0][0]]
        m=len(Lists)
        n=len(Lists[0])
        i=0
        j=0
        while i<m or j<n:
            if i==m-1 and j==n-1:
                break
            if i==m-1:
                res.append(Lists[i][j+1])
                j=j+1
                continue
            if j==n-1:
                res.append(Lists[i+1][j])
                i=i+1
                continue
            a=Lists[i+1][j]
            b=Lists[i][j+1]
            if a<b:
                res.append(a)
                i=i+1
            else:
                res.append(b)
                j=j+1

        print(res,sum(res))


if __name__ == '__main__':
    s = Solution()
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    f=s.traverse(matrix)
    print(f)
