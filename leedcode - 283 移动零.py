'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。

示例 1:
输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]

示例 2:
输入: nums = [0]
输出: [0]
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_count = 0
        # 删除0元素，但是这样做会导致列表长度发生变化，从而导致后续的索引错误
        # for i in range(len(nums)):
            # if nums[i] == 0:
        for num in nums:
            if num != 0: 
                nums[non_zero_count] = num
                non_zero_count += 1
        for i in range(non_zero_count, len(nums)):
            nums[i] = 0
