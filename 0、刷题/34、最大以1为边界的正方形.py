# 给你一个由若干 0 和 1 组成的二维网格 grid，请你找出边界全部由 1 组成的最大 正方形 子网格，并返回该子网格中的元素数量。如果不存在，则返回 0
# 。
#
#
#
#  示例 1：
#
#  输入：grid = [[1,1,1],[1,0,1],[1,1,1]]
# 输出：9
#
#
#  示例 2：
#
#  输入：grid = [[1,1,0,0]]
# 输出：1
#
#
#
#
#  提示：
#
#
#  1 <= grid.length <= 100
#  1 <= grid[0].length <= 100
#  grid[i][j] 为 0 或 1
#
#  Related Topics 动态规划
#  👍 65 👎 0



from typing import List


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        max_l = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                for l in range(0, min(len(grid) - i, len(grid[0]) - j)):
                    if grid[i + l][j] == 0 or grid[i][j + l] == 0:
                        break
                    if len(set(grid[i + l][j:j + l + 1])) == 1 and len(set(g[j + l] for g in grid[i:i + l + 1])) == 1:
                        max_l = max(max_l, l + 1)

        return max_l ** 2


