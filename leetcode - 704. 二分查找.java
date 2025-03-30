class Solution {
    public int search(int[] nums, int target) {
        int right = nums.length - 1, middle = nums.length / 2, left = 0;
        while(left <= right){
            if(nums[middle] == target){
                return middle;
            }else if (nums[middle] < target){
                left = middle + 1;
                middle = left + (right - left) / 2;
            } else if (target < nums[middle]){
                right = middle - 1;
                middle = right / 2;
            } 
        }
        return -1;
    }
}
