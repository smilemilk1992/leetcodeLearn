__author__ = 'haochen214934'


class Solution:
    def traverse(self, Lists,target):
        flag=False
        m=len(Lists)
        n=len(Lists[0])
        for i in range(m):
            if Lists[i][n-1]<target and Lists[i][0]<target:
                continue
            flag=self.check(Lists[i],target)
            if flag:
                break
        return flag

    def check(self,list,targe):#二分法
        low=0
        high=len(list)-1
        while low<=high:
            mid=(low+high)//2
            if targe>list[mid]:
                low=mid+1
            elif targe<list[mid]:
                high=mid-1
            else:
                return True
        return False





if __name__ == '__main__':
    s = Solution()
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    target=13
    f=s.traverse(matrix,target)
    print(f)
