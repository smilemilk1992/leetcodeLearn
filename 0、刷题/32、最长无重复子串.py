class Solution:
    def traverse(self, strs):
        low=0
        high=1
        maxs=0
        while low<=high and high<len(strs):
            if strs[high] not in strs[low:high]:
                high=high+1
            elif high==low:
                low=low+1
                high=high+1
            else:
                low=low+1
            maxs=max(maxs,high-low)
        print(maxs)
        return maxs


if __name__ == '__main__':
    s=Solution()
    strs="absbdbdbdajshas"
    s.traverse(strs)
