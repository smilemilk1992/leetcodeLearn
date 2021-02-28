class Solution:
    #二进制
    def editSum(self, n1,n2):
        while n1>0:
            n1=n1>>1
            print(n1)

    #两个字符串
    '''
    i、j 分别指向 word1、word2 中的某位置（初始指向字符串尾部）
    若 word1[i]=word2[j]，则编辑距离为 0，不需要进行操作，此时需要同时将 i、j 左移。
    若 word1[i]！=word2[j]，则需要进行插入、删除、替换操作使得对应字符相同：
    对 word1 的 i 位置后进行插入字符操作，此时将 j 左移，操作数 +1；
    对 word1 的 i 位置处字符进行替换操作，此时将 i 和 j 同时左移，操作数 +1；
    对 word1 的 i 位置处字符进行删除操作，此时将 i 左移，操作数 +1。
    最终取word1=word2时最小的操作数
    
    执行插入操作 比较word1[0...i] 和word2[0...j-1]
    执行删除操作 比较word1[0...i-1] 和word2[0...j]
    执行替换操作 比较word1[0...i-1] 和word2[0...j-1]
    
    选择上述三个选项中最小的那个+1
    一旦涉及到子问题 可以用自顶向下的递归 和自底向上的动态规划
    '''
    #递归
    def minDistance(self,word1, word2):
        if len(word1) or len(word2):
            return max(len(word1),len(word2))
        if word1[-1]==word2[-1]:
            return self.minDistance(word1[:-1],word2[:-1])
        return 1+min(
            self.minDistance(word1,word2[:-1]),
            self.minDistance(word1[:-1],word2),
            self.minDistance(word1[:-1],word2[:-1])
        )

    #动态规划
    '''
    如果word1[i]==word2[j] 那么dp[i][j]==dp[i-1][j-1]
    否则dp[i][j]=1+min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
    '''
    def minDistanceDp(self,word1, word2):
        n=len(word1)
        m=len(word2)
        if m*n==0:
            return m+n
        dp=[[0]*(m+1) for _ in range(n+1)]

        # 边界状态初始化
        for i in range(n+1):
            dp[i][0]=i
        for j in range(m+1):
            dp[0][j]=j

        # 计算所有 DP 值
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = dp[i - 1][j] + 1
                down = dp[i][j - 1] + 1
                left_down=dp[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    left_down += 1
                dp[i][j]=min(left,down,left_down)
        print(dp[n][m])



if __name__ == '__main__':
    s=Solution()

    word1 = "horse"
    word2 = "hors"
    f=s.minDistanceDp(word1,word2)
    print(f)
