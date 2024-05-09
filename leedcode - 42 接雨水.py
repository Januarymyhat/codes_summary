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
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        left_max[0] = height[0]
        right_max[n - 1] = height[n - 1]

        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        total = 0
        for i in range(n):
            total += min(left_max[i], right_max[i]) - height[i]

        return total
