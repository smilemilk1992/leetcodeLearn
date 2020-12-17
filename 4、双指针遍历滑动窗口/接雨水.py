# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
#
#
#  示例 1：
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
#
#
#  示例 2：
# 输入：height = [4,2,0,3,2,5]
# 输出：9

#  提示：
#
#
#  n == height.length
#  0 <= n <= 3 * 104
#  0 <= height[i] <= 105
#https://blog.csdn.net/weixin_40510799/article/details/89456519
#  Related Topics 栈 数组 双指针


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n <= 2:
            return 0
        i, j = 0, n - 1
        res = 0
        left_max = 0
        right_max = n - 1
        while i < j:
            if height[i] > height[j]:  # 右边低于左边
                if height[right_max] < height[j]:  # 右边当前高度小于右边最大高度
                    right_max = j  # 高度差为当前柱子上面的水量
                    j -= 1
                else:
                    res += height[right_max] - height[j]  # 否则更新右边最大高度
                    j -= 1
            else:  # 左边低于右边
                if height[left_max] < height[i]:
                    left_max = i
                    i += 1
                else:
                    res += height[left_max] - height[i]
                    i += 1
        return res


if __name__ == '__main__':
    s=Solution()
    height=[4,2,3]
    rs=s.trap(height)
    print(rs)