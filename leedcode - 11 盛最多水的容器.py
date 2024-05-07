class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, res = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1
        return res

'''
暴力算法，超时
class Solution:
    def maxArea(self, height: List[int]) -> int:
        outputs = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                if i >= j:
                    j += 1
                outputs = max(min(height[i], height[j]) * (j-i), outputs)
        return outputs
'''
