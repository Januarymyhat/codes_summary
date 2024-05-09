'''
你的解决方案只考虑了从左到右的情况，但是接雨水的问题需要同时考虑从左到右和从右到左两个方向。
class Solution:
    def trap(self, height: List[int]) -> int:
        total = temp = 0
        left, right = 0, 2
        while right < len(height):
            if height[right] >= height[left]:
                total += height[right] - height[left]
                right += 1
            else:
                left = right
        return total
'''
